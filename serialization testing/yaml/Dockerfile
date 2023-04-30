FROM python:latest

WORKDIR /usr/app/src

ADD lib lib
COPY yaml/yaml_testing.py yaml/requirements.txt .

RUN pip install -r requirements.txt
CMD [ "python3", "yaml_testing.py" ]
