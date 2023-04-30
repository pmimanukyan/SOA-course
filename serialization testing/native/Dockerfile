FROM python:latest

WORKDIR /usr/app/src

ADD lib lib
COPY native/native_testing.py .


CMD [ "python3", "native_testing.py" ]
