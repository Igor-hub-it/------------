# Сайт для оценки кадастровой стоимости

Проект разделён на два независимых приложения:

- `frontend` — сайт на `Nuxt 4`, `Vue 3`, `Tailwind CSS`
- `backend` — API на `FastAPI` для отправки заявок на email через почтовый API

## Что уже реализовано

- лендинг с формой заявки
- страницы услуг:
  - оценка движимого имущества
  - оценка нежилой недвижимости
  - оценка жилой недвижимости
  - оценка земельного участка
  - оценка кадастровой стоимости
- страница политики обработки персональных данных
- отправка заявок на email через почтовый API по HTTPS

## Запуск frontend

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

## Запуск backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Перед запуском укажите в `backend/.env` настройки почтового API: `MAIL_API_KEY`, `MAIL_FROM`, `MAIL_TO`.

Для production-деплоя на Timeweb используйте инструкцию `DEPLOY_TIMEWEB.md`.

## API

- `GET /api/health`
- `POST /api/applications`

Пример тела запроса:

```json
{
  "name": "Иван",
  "email": "ivan@example.com",
  "phone": "+7 999 123-45-67",
  "property_type": "Жилая недвижимость",
  "message": "Нужна оценка квартиры для суда."
}
```
