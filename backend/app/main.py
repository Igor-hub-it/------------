import os
from pathlib import Path

import httpx
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


def get_mail_api_settings() -> dict[str, str]:
    api_url = os.getenv("MAIL_API_URL", "https://api.brevo.com/v3/smtp/email").strip()
    api_key = os.getenv("MAIL_API_KEY", "").strip()
    mail_to = os.getenv("MAIL_TO", "").strip()
    mail_from = os.getenv("MAIL_FROM", "").strip()
    mail_from_name = os.getenv("MAIL_FROM_NAME", "Peraks").strip()

    if not all([api_url, api_key, mail_to, mail_from]):
        raise HTTPException(
            status_code=500,
            detail="Почтовый API не настроен. Заполните MAIL_API_KEY, MAIL_FROM и MAIL_TO в backend/.env."
        )

    return {
        "api_url": api_url,
        "api_key": api_key,
        "mail_to": mail_to,
        "mail_from": mail_from,
        "mail_from_name": mail_from_name,
    }


def build_email_text(payload: ApplicationCreate) -> str:
    return "\n".join(
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
    )


def send_application_email(payload: ApplicationCreate) -> None:
    settings = get_mail_api_settings()
    email_payload = {
        "sender": {
            "name": settings["mail_from_name"],
            "email": settings["mail_from"],
        },
        "to": [{"email": settings["mail_to"]}],
        "replyTo": {
            "email": payload.email,
            "name": payload.name,
        },
        "subject": f"Новая заявка: {payload.property_type}",
        "textContent": build_email_text(payload),
    }

    try:
        response = httpx.post(
            settings["api_url"],
            headers={
                "accept": "application/json",
                "api-key": settings["api_key"],
                "content-type": "application/json",
            },
            json=email_payload,
            timeout=15,
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Почтовый API отклонил письмо: {exc.response.text}"
        ) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось отправить письмо через почтовый API: {exc}"
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
