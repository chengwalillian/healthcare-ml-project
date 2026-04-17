#!/bin/bash
set -e

echo "Waiting for postgres..."
python -c "
import socket, time
while True:
    try:
        socket.create_connection(('postgres', 5432), timeout=1)
        break
    except OSError:
        time.sleep(0.5)
"

echo "Checking if patients table needs seeding..."
python -c "
import os, sys
from sqlalchemy import text
from database.db_connection import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text('SELECT COUNT(*) FROM patients'))
        count = result.scalar()
        if count == 0:
            print('Patients table empty, running ingest...')
            sys.exit(1)
        else:
            print(f'Patients table has {count} rows, skipping ingest.')
            sys.exit(0)
except Exception as e:
    print(f'Table check failed ({e}), running ingest...')
    sys.exit(1)
" || python -c "from scripts.ingest import ingest; ingest()"

echo "Checking if model exists..."
if [ ! -f "$MODEL_PIPELINE_PATH" ]; then
    echo "Model not found at $MODEL_PIPELINE_PATH, training..."
    python -m ml.train
    echo "Model training complete"
else
    echo "Model found at $MODEL_PIPELINE_PATH"
fi

echo "Starting application..."
exec python -m app.main