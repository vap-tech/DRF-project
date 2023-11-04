FROM python:3.11
LABEL authors="V. Petrenko"
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
