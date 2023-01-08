FROM python:3.8-alpine

WORKDIR /app

COPY Makefile geometric-service .

RUN make release

EXPOSE 5000
