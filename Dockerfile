FROM python:3.8.2-alpine3.11

MAINTAINER Fernando Cremer "cremerfc@gmail.com"

RUN apk add --update-cache \
    stress-ng

COPY ./Requirements.txt /Requirements.txt

WORKDIR /

RUN pip3 install -r Requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
