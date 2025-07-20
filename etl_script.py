import pandas as pd
from sqlalchemy import create_engine
import logging
import sys
import os

# ---------------------- Logging Setup ----------------------
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------- Database Configuration -------------------
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"
TABLE_NAME = "tyroo_data"
CSV_PATH = "Data/Tyroo-dummy-data.csv" 

# ------------------- Create SQLAlchemy Engine -------------------
try:
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        echo=False
    )
    logging.info("✅ Database engine created successfully.")
except Exception as e:
    logging.error(f"❌ Failed to create engine: {e}")
    sys.exit(1)

# ------------------- Read CSV and Insert in Chunks -------------------
CHUNK_SIZE = 10000
first_chunk = True

try:
    for chunk in pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE):
        chunk = chunk.where(pd.notnull(chunk), None)

        
        chunk.to_sql(
            TABLE_NAME,
            con=engine,
            if_exists='replace' if first_chunk else 'append',
            index=False,
            method='multi'
        )
        logging.info(f"Inserted chunk of {len(chunk)} records")
        first_chunk = False

    logging.info(f"✅ Table '{TABLE_NAME}' created and fully populated from CSV.")

except Exception as e:
    logging.error(f"❌ ETL Failed: {e}")
    sys.exit(1)
