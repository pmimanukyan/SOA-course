import pickle

from lib.test import test_struct
from lib.UDPServer import send_answer
from lib.tester import test

def serialize():
    return pickle.dumps(test_struct)

def deserialize(serialized):
    return pickle.loads(serialized)

serialization_time, deserialization_time = test(serialize, deserialize)
send_answer("native", f'native testing time: {serialization_time}, {deserialization_time}\n')
