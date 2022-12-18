FROM python:3.8-alpine

ARG run_env
ENV env $run_env

LABEL "channel"="Zapel"
LABEL "creator"="Zapel community"

WORKDIR ./usr/lessons
COPY requirements.txt .

RUN apk update && apk upgrade && apk add bash
RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -m "$env" -s -v tests/*



