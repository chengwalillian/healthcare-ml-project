FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files
COPY pyproject.toml uv.lock* ./

# Install dependencies including Airflow 3 required providers
RUN uv pip install --system -e . && \
    uv pip install --system \
        asyncpg \
        apache-airflow-providers-fab \
        apache-airflow-providers-postgres

# Copy application code
COPY . .

ENV PYTHONPATH=/app
ENV AIRFLOW_HOME=/app/airflow

EXPOSE 5000