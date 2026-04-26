import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import AliasChoices, BaseModel, ConfigDict, EmailStr, Field, field_validator

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env", override=True)


class ApplicationCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=40)
    property_type: str = Field(
        min_length=2,
        max_length=120,
        validation_alias=AliasChoices("property_type", "propertyType"),
    )
    message: str = Field(min_length=5, max_length=4000)

    @field_validator("name", "phone", "property_type", "message", mode="before")
    @classmethod
    def strip_string_fields(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip()
        return value


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str
    message: str


def get_allowed_origins() -> list[str]:
    raw_origins = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000"
    )
    return [origin.strip() for origin in raw_origins.split(",") if origin.strip()]


def get_smtp_settings() -> dict[str, str | int | bool]:
    smtp_host = os.getenv("SMTP_HOST", "").strip()
    smtp_user = os.getenv("SMTP_USER", "").strip()
    smtp_password = os.getenv("SMTP_PASSWORD", "").strip().replace(" ", "")
    mail_to = os.getenv("MAIL_TO", "").strip()
    mail_from = os.getenv("MAIL_FROM", smtp_user).strip()
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_starttls = os.getenv("SMTP_STARTTLS", "false").lower() == "true"

    if not all([smtp_host, smtp_user, smtp_password, mail_to, mail_from]):
        raise HTTPException(
            status_code=500,
            detail="SMTP не настроен. Заполните SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, MAIL_FROM и MAIL_TO в backend/.env."
        )

    return {
        "smtp_host": smtp_host,
        "smtp_port": smtp_port,
        "smtp_user": smtp_user,
        "smtp_password": smtp_password,
        "smtp_starttls": smtp_starttls,
        "mail_to": mail_to,
        "mail_from": mail_from,
    }


def build_email(payload: ApplicationCreate, mail_from: str, mail_to: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = f"Новая заявка: {payload.property_type}"
    message["From"] = mail_from
    message["To"] = mail_to
    message["Reply-To"] = payload.email
    message.set_content(
        "\n".join(
            [
                "На сайте оставлена новая заявка.",
                "",
                f"Имя: {payload.name}",
                f"Email: {payload.email}",
                f"Телефон: {payload.phone}",
                f"Тип недвижимости: {payload.property_type}",
                "",
                "Сообщение:",
                payload.message,
            ]
        ),
        charset="utf-8",
    )
    return message


def send_application_email(payload: ApplicationCreate) -> None:
    settings = get_smtp_settings()
    email_message = build_email(
        payload=payload,
        mail_from=str(settings["mail_from"]),
        mail_to=str(settings["mail_to"]),
    )

    try:
        if settings["smtp_starttls"]:
            with smtplib.SMTP(str(settings["smtp_host"]), int(settings["smtp_port"])) as server:
                server.starttls()
                server.login(str(settings["smtp_user"]), str(settings["smtp_password"]))
                server.send_message(email_message)
        else:
            with smtplib.SMTP_SSL(str(settings["smtp_host"]), int(settings["smtp_port"])) as server:
                server.login(str(settings["smtp_user"]), str(settings["smtp_password"]))
                server.send_message(email_message)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось отправить письмо: {exc}"
        ) from exc


app = FastAPI(
    title="Property Valuation API",
    version="1.0.0",
    summary="API для приёма заявок с сайта оценки кадастровой стоимости"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/applications", response_model=ApplicationResponse, status_code=201)
def create_application(payload: ApplicationCreate) -> ApplicationResponse:
    send_application_email(payload)
    return ApplicationResponse(
        status="received",
        message="Заявка отправлена на почту."
    )
