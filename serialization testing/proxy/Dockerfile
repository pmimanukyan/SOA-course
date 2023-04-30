FROM python:latest

WORKDIR /proxy

ADD lib lib
COPY proxy/UDPClient.py .

CMD [ "python3", "UDPClient.py" ]