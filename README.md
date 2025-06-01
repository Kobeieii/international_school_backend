# Django Backend with PostgreSQL and Docker Compose

This Django backend project uses PostgreSQL as the database and Docker Compose to manage services.

---

## 🧰 Prerequisites

- Python 3.9+
- Docker & Docker Compose
- (Recommended) Virtual Environment

---

## 📝 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Setup environment variables

Copy the `.env_example` file to `.env` and fill in your values:

```bash
cp .env_example .env
```

### 3. Start PostgreSQL with Docker Compose

```bash
docker-compose up -d
```

### 4. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 5. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

(Optional) Create superuser:

```bash
python manage.py createsuperuser
```

### 7. Start development server

```bash
python manage.py runserver
```

---

## 🐘 PostgreSQL Setup

The database is managed by Docker. Configuration comes from the `.env` file:

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Example Django `settings.py`:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

