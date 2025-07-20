# tyroo_assignment
# ETL Pipeline: Load Large CSV into PostgreSQL

This project reads a large CSV file in chunks, cleans it by replacing empty values with `NULL`, and loads it into a PostgreSQL database table using Python, Pandas, and SQLAlchemy.

---

## Features

- Chunk-wise processing to avoid memory issues
- Converts missing values to NULL
- Automatically creates the PostgreSQL table from DataFrame
- Appends data in chunks for performance
- Logs errors and progress to `logs/etl.log`

---

## Tech Stack

- Python 3.8+
- Pandas
- SQLAlchemy
- PostgreSQL
- psycopg2

---

## Project Structure

```
.
├── Data/
│   └── Tyroo-dummy-data.csv
├── logs/
│   └── etl.log
├── etl_script.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-folder>
```

### 2. Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

### 3. Configure the Database

Ensure you have a PostgreSQL server running and update the credentials in `etl_script.py`:

```python
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"
```

Also update the path to your CSV file:

```python
CSV_PATH = "Data/Tyroo-dummy-data.csv"
```

---

### 4. Run the Script

```bash
python etl_script.py
```

Logs will be stored in the `logs/etl.log` file.

---
