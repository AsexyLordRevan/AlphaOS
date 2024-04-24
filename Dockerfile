FROM python:3.8

WORKDIR /docker

RUN apt update && apt install nano wget whiptail -y

COPY requirements.txt /docker


RUN /usr/local/bin/python3 -m pip install -r /docker/requirements.txt

COPY . /docker

RUN mkdir /data && mv /docker/configs /data/.config

WORKDIR /data

ARG BUILD=undefined
ARG TIME=undefined

RUN echo "$BUILD" > /buildct && echo "$TIME" > /buildtm

CMD [ "/usr/local/bin/python3", "/docker/main.py", "--inContainer=TRUE" ]