FROM python:latest

WORKDIR /usr/app/src

ADD lib lib
COPY xml/xml_testing.py xml/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "xml_testing.py" ]
