# Renewable Energy Dashboard — Django Backend

Django REST Framework backend for the Renewable Energy Management Dashboard.

---

## Requirements

- Python 3.10 or higher
- pip

---

## Setup Instructions

### 1. Open a terminal and navigate to the backend folder

```
cd "path\to\New folder\backend"
```

### 2. Create a virtual environment

```
python -m venv venv
```

### 3. Activate the virtual environment

Windows:
```
venv\Scripts\activate
```

macOS / Linux:
```
source venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Navigate into the Django project

```
cd renewable_backend
```

### 6. Apply migrations

```
python manage.py migrate
```

### 7. Create a superuser (for Django Admin)

```
python manage.py createsuperuser
```

### 8. Start the development server

```
python manage.py runserver
```

The backend will be available at:
```
http://127.0.0.1:8000
```

---

## Available Endpoints (this step)

| URL | Description |
|-----|-------------|
| `GET /api/` | Health check — confirms backend is running |
| `GET /admin/` | Django Admin panel |

---

## Planned Endpoints (next step)

| URL | Description |
|-----|-------------|
| `GET /api/energy/` | Current energy readings |
| `GET /api/energy/history/` | Historical energy data |
| `GET /api/battery/` | Battery status |
| `GET /api/battery/history/` | Battery history |
| `GET /api/street-lights/` | Street light status |
| `GET /api/street-lights/history/` | Street light history |
| `GET /api/faults/` | Fault records |
| `GET /api/dashboard/` | Aggregated dashboard data |
| `GET /api/environment/` | CO2 and cost savings |

---

## CORS Configuration

The backend is configured to accept requests from the React frontend at:
```
http://localhost:3000
```

This is set in `config/settings.py` under `CORS_ALLOWED_ORIGINS`.

---

## Project Structure

```
backend/
├── requirements.txt
├── .gitignore
├── README.md
└── renewable_backend/
    ├── manage.py
    ├── db.sqlite3          (created after migrate)
    └── config/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── asgi.py
```

---

## Future Architecture

```
IoT Sensors (ESP32)
       ↓
   Wi-Fi / MQTT
       ↓
Django REST API  ←── this backend
       ↓
   SQLite → PostgreSQL (production)
       ↓
React Dashboard (port 3000)
```

---

## Notes

- `DEBUG = True` — development only, change before deployment
- `SECRET_KEY` — replace with a secure key before production
- SQLite is used for development; PostgreSQL will be added later
- Authentication will be added in a future step
