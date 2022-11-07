FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY pyproject.toml ./
RUN pip install poetry --no-cache-dir && poetry config virtualenvs.create false && poetry install --no-dev

COPY main.py /app/main.py
