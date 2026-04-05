# CureQuest

CureQuest is a Flask-based backend service that suggests possible diseases from a list of symptoms using a MySQL medical knowledge base.

## Overview

The project contains:

- A REST API for diagnosis requests
- SQL schema and seed data for diseases, symptoms, tests, medicines, and dosages
- Logic that ranks diseases by symptom match count

This repository is educational and should not be used as a replacement for professional medical advice.

## Features

- Symptom-to-disease matching via SQL joins
- Ranked disease results (`match_count`)
- MySQL relational schema for clinical entities
- CORS-enabled API for frontend integration

## Tech Stack

- Python 3.9+
- Flask
- Flask-CORS
- MySQL
- mysql-connector-python

## Repository Structure

- `app.py`: Flask API entry point
- `logic.py`: disease matching query logic
- `db_config.py`: database settings (and connection helper, if implemented)
- `SQL (2).txt`: database schema
- `SQL data (2).txt`: seed/sample data

## API

### `POST /diagnose`

Accepts a JSON payload with symptom names and returns possible diseases.

Request:

```json
{
  "symptoms": ["Fever", "Headache", "Fatigue"]
}
```

Successful response:

```json
{
  "possible_diseases": [
    {
      "disease_id": 20,
      "name": "Dengue Fever",
      "description": "A mosquito-borne viral infection causing severe flu-like illness and sometimes bleeding.",
      "match_count": 3
    }
  ]
}
```

Validation error response:

```json
{
  "error": "No symptoms provided"
}
```

## Local Setup

### 1. Open the CureQuest folder

If you are working from the parent repository (`100_days_of_ml`):

```bash
cd curequest
```

If you copied this folder as a standalone project, open this directory in your terminal first.

### 2. Create virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create and seed database

Run the SQL files in this order:

1. `SQL (2).txt`
2. `SQL data (2).txt`

Example in MySQL shell:

```sql
SOURCE "path/to/SQL (2).txt";
SOURCE "path/to/SQL data (2).txt";
```

### 5. Configure database credentials

Update `db_config.py` with your MySQL connection details.

### 6. Run the server

```bash
python app.py
```

The API starts on `http://127.0.0.1:5001`.

## Quick Test

```bash
curl -X POST http://127.0.0.1:5001/diagnose \
  -H "Content-Type: application/json" \
  -d "{\"symptoms\":[\"Fever\",\"Cough\"]}"
```

## Notes

- `logic.py` imports `get_db_connection` from `db_config.py`. Ensure this function exists and returns a valid MySQL connection.
- Move credentials to environment variables before any production deployment.

## Suggested Next Improvements

- Add input validation and symptom normalization
- Add confidence scoring and thresholding
- Add automated tests for API and matching logic
- Add Docker support
- Add CI for linting and tests

## License

Add your preferred license (for example, MIT).
