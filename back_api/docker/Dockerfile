FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev python-dev

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]