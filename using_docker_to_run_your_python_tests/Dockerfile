FROM python:3.10.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_CREATE=false

COPY src/ src/ 
COPY tests/ tests/
COPY poetry.lock pyproject.toml ./

RUN pip install -U pip && \
    pip install poetry==1.5.1 && \
    poetry install --no-interaction --no-cache --without dev

ENTRYPOINT ["pytest", "-s", "tests"]
