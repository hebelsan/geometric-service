FROM python:3.8-slim-buster

ENV ALPHA true

WORKDIR /app

COPY geometric-service .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]

EXPOSE 5000
