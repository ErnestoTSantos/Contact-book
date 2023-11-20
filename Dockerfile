FROM python:3.11-slim

RUN apt update

WORKDIR /app

RUN useradd appuser && chown appuser ./

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local

# Copy dependency definition to cache
COPY --chown=appuser poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY --chown=appuser . ./

EXPOSE 8080

USER appuser