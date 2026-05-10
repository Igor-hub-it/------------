# Деплой проекта на Timeweb Cloud

Инструкция рассчитана на сервер Ubuntu 24.04, домен `peraks.ru` и IP `186.246.14.163`.

## 1. DNS

В DNS-зоне домена должны быть A-записи:

```text
A    @      186.246.14.163
A    www    186.246.14.163
```

Проверка после обновления DNS:

```bash
nslookup peraks.ru
nslookup www.peraks.ru
```

Обе команды должны вернуть `186.246.14.163`.

## 2. Подключение к серверу

В Termius подключитесь:

```bash
ssh root@186.246.14.163
```

Обновите систему и установите базовые пакеты:

```bash
apt update && apt upgrade -y
apt install -y nginx certbot python3-certbot-nginx python3-venv git curl ufw
```

Установите Node.js LTS:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
node --version
npm --version
```

Для сервера с 1 ГБ RAM добавьте swap, чтобы сборка Nuxt не упала из-за нехватки памяти:

```bash
fallocate -l 2G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
free -h
```

## 3. Загрузка проекта на сервер

Создайте папку:

```bash
mkdir -p /var/www/peraks
```

Если проект будет загружаться через SFTP в Termius, загрузите содержимое локальной папки проекта в `/var/www/peraks`.

Если проект есть в Git:

```bash
git clone YOUR_REPOSITORY_URL /var/www/peraks
```

Перейдите в проект:

```bash
cd /var/www/peraks
```

## 4. Backend

Создайте production env:

```bash
cd /var/www/peraks/backend
cp .env.example .env
nano .env
```

Для Brevo API заполните:

```env
ALLOWED_ORIGINS=https://peraks.ru,https://www.peraks.ru
MAIL_API_URL=https://api.brevo.com/v3/smtp/email
MAIL_API_KEY=your-brevo-api-key
MAIL_FROM=verified-sender@example.com
MAIL_FROM_NAME=Peraks
MAIL_TO=recipient@example.com
```

Важно: `MAIL_FROM` должен быть подтверждённым отправителем в Brevo.

После заполнения закройте доступ к env-файлу:

```bash
chmod 600 /var/www/peraks/backend/.env
```

Установите backend-зависимости:

```bash
cd /var/www/peraks/backend
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate
```

Создайте systemd-сервис:

```bash
nano /etc/systemd/system/peraks-backend.service
```

Вставьте:

```ini
[Unit]
Description=Peraks FastAPI backend
After=network.target

[Service]
WorkingDirectory=/var/www/peraks/backend
EnvironmentFile=/var/www/peraks/backend/.env
ExecStart=/var/www/peraks/backend/.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Запустите:

```bash
systemctl daemon-reload
systemctl enable --now peraks-backend
systemctl status peraks-backend --no-pager
```

Проверка:

```bash
curl http://127.0.0.1:8000/api/health
```

Ожидаемый ответ:

```json
{"status":"ok"}
```

## 5. Frontend

Создайте production env:

```bash
cd /var/www/peraks/frontend
cp .env.production.example .env.production
nano .env.production
```

Содержимое:

```env
NUXT_PUBLIC_API_BASE=https://peraks.ru
```

Соберите Nuxt:

```bash
cd /var/www/peraks/frontend
npm install
npm run build
```

Создайте systemd-сервис:

```bash
nano /etc/systemd/system/peraks-frontend.service
```

Вставьте:

```ini
[Unit]
Description=Peraks Nuxt frontend
After=network.target

[Service]
WorkingDirectory=/var/www/peraks/frontend
Environment=NODE_ENV=production
Environment=HOST=127.0.0.1
Environment=PORT=3000
EnvironmentFile=/var/www/peraks/frontend/.env.production
ExecStart=/usr/bin/node .output/server/index.mjs
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Запустите:

```bash
systemctl daemon-reload
systemctl enable --now peraks-frontend
systemctl status peraks-frontend --no-pager
```

Проверка:

```bash
curl -I http://127.0.0.1:3000
```

## 6. Nginx

Создайте конфиг:

```bash
nano /etc/nginx/sites-available/peraks.ru
```

Вставьте:

```nginx
server {
    listen 80;
    server_name peraks.ru www.peraks.ru;

    client_max_body_size 10m;

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Включите сайт:

```bash
ln -s /etc/nginx/sites-available/peraks.ru /etc/nginx/sites-enabled/peraks.ru
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl reload nginx
```

## 7. Firewall

Откройте SSH, HTTP и HTTPS:

```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
ufw status
```

## 8. SSL

После того как DNS начал отдавать `186.246.14.163`, выпустите сертификат:

```bash
certbot --nginx -d peraks.ru -d www.peraks.ru
```

Проверьте автопродление:

```bash
certbot renew --dry-run
```

## 9. Финальная проверка

Проверьте сайт:

```bash
curl -I https://peraks.ru
curl https://peraks.ru/api/health
```

Проверьте заявку:

```bash
curl -X POST https://peraks.ru/api/applications \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Тест",
    "email": "test@example.com",
    "phone": "+79991234567",
    "property_type": "Жилая недвижимость",
    "message": "Тестовая заявка с production-сервера."
  }'
```

Ожидаемый ответ:

```json
{"status":"received","message":"Заявка отправлена на почту."}
```

## 10. Полезные команды диагностики

Backend:

```bash
systemctl status peraks-backend --no-pager
journalctl -u peraks-backend -n 100 --no-pager
```

Frontend:

```bash
systemctl status peraks-frontend --no-pager
journalctl -u peraks-frontend -n 100 --no-pager
```

Nginx:

```bash
nginx -t
journalctl -u nginx -n 100 --no-pager
```
