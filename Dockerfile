FROM python:3.11 as builder

RUN apt-get update && apt-get install libpq-dev postgresql postgresql-contrib -y

COPY requirements.txt /tmp/requirements.txt
RUN pip wheel -r /tmp/requirements.txt --no-cache-dir -w /wheels

FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install libpq-dev -y

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY robot_ui /code/robot_ui
WORKDIR /code/robot_ui

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
