FROM python:3.9-alpine

RUN apk update && apk add build-base libffi-dev

COPY . .

RUN pip3 install ansible