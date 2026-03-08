# Docker Deploy Guide

## 1. Prepare `.env`

Create `.env` from `.env.example` and set production values.

Example for VPS with Docker Compose and Postgres:

```env
DEBUG=False
SECRET_KEY=replace-with-strong-secret
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,server-ip
CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://www.your-domain.com
DATABASE_URL=postgresql://portfolio:strong-password@db:5432/portfolio
POSTGRES_DB=portfolio
POSTGRES_USER=portfolio
POSTGRES_PASSWORD=strong-password
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
GUNICORN_WORKERS=3
GUNICORN_TIMEOUT=60
```

If you want a quick web-only start without Postgres, set:

```env
DEBUG=False
SECRET_KEY=replace-with-strong-secret
ALLOWED_HOSTS=server-ip,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://server-ip:8000
DATABASE_URL=
```

## 2. Build and start

```bash
docker compose up --build -d
```

Quick web-only start:

```bash
docker compose up --build -d web
```

## 3. View logs

```bash
docker compose logs -f web
docker compose logs -f db
```

## 4. Restart services

```bash
docker compose restart web
docker compose restart db
```

## 5. Stop services

```bash
docker compose down
```

To remove containers and anonymous network only:

```bash
docker compose down
```

To also remove Postgres volume data:

```bash
docker compose down -v
```

## 6. Run migrations manually

```bash
docker compose exec web python manage.py migrate
```

## 7. Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

## 8. Collect static manually

```bash
docker compose exec web python manage.py collectstatic --noinput
```

## 9. Rebuild after code changes

```bash
docker compose up --build -d
```

## 10. Useful service commands

Open shell in web container:

```bash
docker compose exec web sh
```

Check container status:

```bash
docker compose ps
```

Restart only Django service:

```bash
docker compose restart web
```

Tail the last 100 web logs:

```bash
docker compose logs --tail=100 web
```

## 11. VPS notes

- Install Docker and Docker Compose plugin
- Copy project to server
- Create `.env`
- Run `docker compose up --build -d`
- Put Nginx in front later as a separate step if needed

## 12. Post-start verification

Check application:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/api/projects/
curl http://127.0.0.1:8000/api/skills/
curl http://127.0.0.1:8000/api/case-studies/
curl http://127.0.0.1:8000/admin/
```

Check database container health:

```bash
docker compose ps
```
