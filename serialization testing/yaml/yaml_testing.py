import yaml

from lib.test import test_struct
from lib.UDPServer import send_answer
from lib.tester import test

def serialize():
    return yaml.dump(test_struct)

def deserialize(serialized):
    return yaml.load(serialized, yaml.BaseLoader)

serialization_time, deserialization_time = test(serialize, deserialize)
send_answer("yaml", f'yaml testing time: {serialization_time}, {deserialization_time}\n')
