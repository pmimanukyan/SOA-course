FROM python:latest

WORKDIR /usr/app/src

ADD lib lib
COPY apache_avro/avro_testing.py apache_avro/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "avro_testing.py" ]
