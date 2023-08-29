FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD "gunicorn back_api.wsgi  -b 0.0.0.0:8000"