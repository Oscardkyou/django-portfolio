# Dauren Askarov Portfolio

Django portfolio project for a Python Backend / AI Engineer. The project combines a modern portfolio UI with a production-ready Django backend, admin-managed content, and a clean foundation for future AI and ML features.

## Stack

- Python 3.11+
- Django 5
- Bootstrap + custom dark theme UI
- Pillow
- WhiteNoise
- Gunicorn
- SQLite locally
- PostgreSQL-ready via `DATABASE_URL`

## Implemented

- Home, About, Projects, Skills, Contact pages
- Safe fallback logic for `/about/` when `Author` is missing
- Django admin configuration for Author, Work, Skill, Category, Message, CaseStudy
- API endpoints:
  - `/api/projects`
  - `/api/skills`
  - `/api/case-studies`
  - placeholder `/api/ask-ai`
  - placeholder `/api/predict`
- Featured projects, architecture blocks, performance metrics, GitHub activity, SEO tags
- Production-oriented settings with env-based configuration

## Local setup

```bash
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Create `.env`

Populate `.env` based on `.env.example`.

Minimum local example:

```env
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Migrations

```bash
source .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
```

## Create superuser

```bash
source .venv/bin/activate
python manage.py createsuperuser
```

## Run locally

```bash
source .venv/bin/activate
python manage.py runserver 127.0.0.1:8000
```

## Run with Docker

```bash
cp .env.example .env
docker compose up --build -d
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`

Stop:

```bash
docker compose down
```

## Verification

### Pages

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/about/`
- `http://127.0.0.1:8000/projects/`
- `http://127.0.0.1:8000/skills/`
- `http://127.0.0.1:8000/contact/`

### API

```bash
curl http://127.0.0.1:8000/api/projects/
curl http://127.0.0.1:8000/api/skills/
curl http://127.0.0.1:8000/api/case-studies/
curl http://127.0.0.1:8000/api/ask-ai/
curl http://127.0.0.1:8000/api/predict/
```

## Production deploy preparation

```bash
source .venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 127.0.0.1:8000
```

Use Nginx in front of Gunicorn. Detailed steps are in `DEPLOY.md`.
For Docker-based deploy, see `DOCKER_DEPLOY.md`.

## Environment variables

Prepared in `.env.example`:

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `OPENAI_API_KEY`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`
- `AWS_S3_REGION_NAME`
- `MLFLOW_TRACKING_URI`
- `TELEGRAM_BOT_TOKEN`

## Architecture foundation for future features

### AI chatbot

Prepared foundation:
- `portfolio/services.py`
- placeholder endpoint `/api/ask-ai`
- `ai/` directory for prompts, adapters, and knowledge base

### MLflow demo

Prepared foundation:
- placeholder endpoint `/api/predict`
- `ml_demo/` directory for training/inference code
- `MLFLOW_TRACKING_URI` env variable
- ignored local experiment artifacts in `.gitignore`

### Case studies

Prepared foundation:
- `CaseStudy` model
- `/api/case-studies`
- admin-ready content structure for problem / solution / stack / metrics / architecture / links / featured flag

## Roadmap

- AI chatbot on portfolio
- MLflow demo with simple logistics model
- project case studies with metrics and architecture
- richer knowledge base for portfolio Q&A
- prediction API backed by trained demo model

## Notes before GitHub push

Make sure these are **not** committed:

- `.env`
- `.venv/`
- `db.sqlite3`
- `media/`
- `staticfiles/`
- `mlruns/`
- secrets / keys / credentials

## Deploy checklist

See `DEPLOY.md` for the server deployment sequence.