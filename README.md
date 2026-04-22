# ReactQuest – Backend

FastAPI-Backend mit PostgreSQL-Datenbankanbindung über SQLAlchemy.

## Voraussetzungen

- Python 3.11+
- PostgreSQL läuft via Docker Compose (localhost:5432)

## Setup

```bash
# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Backend starten
uvicorn app.main:app --reload
```

## API

- `GET /` – Health Check
- `GET /lessons` – Alle Lessons
- `GET /quiz-questions` – Alle Quizfragen mit Antworten
- `GET /docs` – Swagger UI

## Datenbankverbindung

```
Host:     localhost:5432
Datenbank: appdb
Benutzer:  appuser
Passwort:  supersecret123
```

## Projektstruktur

```
app/
├── main.py              # FastAPI-App, Startup-Events
├── core/
│   ├── config.py        # Konfiguration & DATABASE_URL
│   ├── db.py            # Engine, Base, SessionLocal
│   └── deps.py          # get_db() Dependency
├── models/
│   ├── lesson.py        # LessonDB ORM-Modell
│   └── quiz.py          # QuizQuestionDB + AnswerOptionDB
├── schemas/
│   ├── lesson.py        # LessonRead Pydantic-Schema
│   └── quiz.py          # QuizQuestionRead + AnswerOptionRead
├── routers/
│   ├── lessons.py       # GET /lessons
│   └── quiz.py          # GET /quiz-questions
├── services/
│   └── seed_service.py  # JSON-Daten in DB importieren
└── data/
    ├── lessons.json
    └── quiz_questions.json
```
