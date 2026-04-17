#!/bin/bash
set -e

# Ensure Airflow home exists
mkdir -p /app/airflow/logs /app/airflow/plugins

echo "Running Airflow DB migrations..."
airflow db migrate || true  # Skip if already migrated

echo "Creating admin user if not exists..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin 2>/dev/null || echo "Admin user already exists"

echo "Starting Airflow: $@"
exec airflow "$@"