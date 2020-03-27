FROM python:3.8.2-alpine3.11

MAINTAINER Fernando Cremer "cremerfc@gmail.com"

RUN apk add --update-cache \
    stress-ng

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]