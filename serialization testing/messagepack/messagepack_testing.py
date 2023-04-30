import msgpack

from lib.test import test_struct
from lib.UDPServer import send_answer
from lib.tester import test


def serialize():
    return msgpack.dumps(test_struct.__dict__)

def deserialize(serialized):
    return msgpack.loads(serialized)

serialization_time, deserialization_time = test(serialize, deserialize)
send_answer("messagepack", f'messagepack testing time: {serialization_time}, {deserialization_time}\n')