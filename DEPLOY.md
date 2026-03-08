# Deploy Guide

## VPS deploy checklist

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Create `.env`
5. Run migrations
6. Collect static files
7. Create superuser
8. Run Gunicorn
9. Configure Nginx
10. Restart services

## Commands

```bash
git clone <your-repo-url>
cd django-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
gunicorn config.wsgi:application --bind 127.0.0.1:8000
```

## Nginx upstream example

```nginx
server {
    listen 80;
    server_name example.com;

    location /static/ {
        alias /path/to/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/project/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Systemd note
Create a service for Gunicorn and restart it after every deploy.
