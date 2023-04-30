import timeit
import fastavro
from io import BytesIO

from lib.UDPServer import send_answer
from lib.tester import test

schema = fastavro.parse_schema({
    "namespace": "example.avro",
    "type": "record",
    "name": "Object",
    "fields": [
        {"name": "str", "type": "string"},
        {"name": "list_", "type": {"type": "array", "items": "int"}},
        {"name": "dict_", "type": {"type": "map", "values": "string"}}
    ]
})

test_struct = {"str": "It's better to have a short life that is full of what you like doing than a long life spent in a miserable way. Alan Watts", "list_": [i for i in range(10)], "dict_": {str(i): str(i) for i in range(10)}}

def serialize():
    buffer = BytesIO()
    fastavro.schemaless_writer(buffer, schema, test_struct)
    buffer.seek(0)
    serialized = buffer.read()
    return buffer

def deserialize(buffer):
    fastavro.schemaless_writer(BytesIO(), schema, test_struct)
    buffer.seek(0)
    fastavro.schemaless_reader(buffer, schema)

starttime = timeit.default_timer()
buffer = serialize()
serialization_time = timeit.default_timer() - starttime

starttime = timeit.default_timer()
serialized = deserialize(buffer)
deserialization_time = timeit.default_timer() - starttime

send_answer("apache_avro", f'apache_avro testing time: {serialization_time}, {deserialization_time}\n')