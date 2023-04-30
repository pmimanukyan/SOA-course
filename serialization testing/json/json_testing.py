import json

from lib.test import test_struct
from lib.UDPServer import send_answer
from lib.tester import test

def serialize():
    return json.dumps(test_struct.__dict__)

def deserialize(serialized):
    json.loads(serialized)


serialization_time, deserialization_time = test(serialize, deserialize)
send_answer('json', f'json testing time: {serialization_time}, {deserialization_time}\n')