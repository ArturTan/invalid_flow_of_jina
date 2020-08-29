FROM ubuntu:latest
ENV TZ=Europe/Kiev
WORKDIR /
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

ADD ./requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt

ADD . /

ENTRYPOINT ["python3", "main.py"]