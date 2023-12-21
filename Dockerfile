FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .


CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --preload
