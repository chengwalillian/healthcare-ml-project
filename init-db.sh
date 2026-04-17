#!/bin/bash
set -e

# Create user if doesn't exist
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    DO \$\$
    BEGIN
        IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'health_app') THEN
            CREATE USER health_app WITH PASSWORD 'password';
        END IF;
    END
    \$\$;

    -- Create database if doesn't exist
    SELECT 'CREATE DATABASE health'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'health')\gexec

    -- Grant privileges
    GRANT ALL PRIVILEGES ON DATABASE health TO health_app;
    ALTER USER health_app WITH PASSWORD 'password';
EOSQL

echo "Database initialization complete"