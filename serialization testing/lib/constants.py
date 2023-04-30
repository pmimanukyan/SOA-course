import os

MULTICAST_GROUP = os.getenv("MULTICAST_GROUP", default="224.0.0.0")

PROXY_PORT = 2000
UNICAST_PORT = 2001
MULTICAST_PORT = 2002

BUFSIZE = 128

formats = ["native", "json", "apache_avro", "xml", "protobuf", "yaml", "messagepack"]