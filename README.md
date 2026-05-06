# SparkUp

Production-ready full-stack starter for a social platform with richer interactive features.

## Tech Stack

- **Backend:** Django, DRF, SimpleJWT, Channels, Celery
- **Frontend:** React, Vite, Redux Toolkit, React Query, Tailwind CSS
- **Data/Infra:** PostgreSQL, Redis, Nginx, Docker Compose
- **Docs:** OpenAPI/Swagger via drf-spectacular
- **Tests:** pytest + Vitest/Testing Library

## Architecture

```text
SparkUp/
├─ backend/
│  ├─ apps/
│  │  ├─ accounts profiles matching chat posts stories communities events notifications ai_features adminpanel common
│  ├─ config/
│  ├─ docker/
│  ├─ requirements/
├─ frontend/
│  └─ src/{api,auth,components,layouts,pages,routes,hooks,context,redux,services,utils,websocket,assets}
├─ deploy/nginx/
└─ docker-compose.yml
```

## Core Capabilities Included

- JWT register/login/logout with role-ready user model
- Phase 2 auth flows: email verification, forgot/reset password, token refresh, user block/unblock
- Modular API-first backend with `/api/v1/` versioning
- Swipe, match, chat room, message, post, story, event, community, notification models + REST endpoints
- Phase 2 messaging: edit/delete/seen actions, reply/media-ready fields, typing event support
- WebSocket consumers for chat and real-time notifications
- Admin stats endpoint with role-based access guard
- Filtering/search/ordering and throttling defaults
- OpenAPI schema at `/api/schema/` and Swagger at `/api/docs/`
- Dockerized local/prod-like environment
- Mobile-friendly React dark UI scaffold and feature pages

## Quick Start

1. Copy env:
   - `cp .env.example .env`
2. Start everything:
   - `docker compose up --build`
3. Backend:
   - API root: `http://localhost/api/v1/`
   - Docs: `http://localhost/api/docs/`
4. Frontend:
   - `http://localhost/`

## Local Dev Without Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements/base.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Testing

- Backend: `cd backend && pytest`
- Frontend: `cd frontend && npm test`

## Deployment Notes

- `gunicorn + uvicorn` worker is configured for ASGI
- Nginx reverse proxy includes API and WebSocket forwarding
- Celery worker/beat configured with Redis broker
- Use environment variables for all secrets and runtime settings

## Next Expansion Points

- Complete password reset + email verification flows
- Add media upload pipelines (S3/Cloudinary)
- Implement AI services in `apps/ai_features`
- Add RBAC policy classes per module
- Integrate push notifications and social OAuth providers
