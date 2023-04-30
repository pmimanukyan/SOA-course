FROM python:latest

WORKDIR /usr/app/src

ADD lib lib
COPY messagepack/messagepack_testing.py messagepack/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "messagepack_testing.py" ]
