FROM python:3.11

RUN apt-get update && apt-get install libpq-dev postgresql postgresql-contrib -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir

COPY robot_ui /code/robot_ui
WORKDIR /code/robot_ui

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
