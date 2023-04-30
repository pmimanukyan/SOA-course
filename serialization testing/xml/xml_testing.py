from lib.UDPServer import send_answer
from lib.tester import test

from dict2xml import dict2xml
import xmltodict


def serialize():
    return dict2xml({'1': '2', '3': '4'}, wrap="object")

def deserialize(serialized):
    return xmltodict.parse(serialized)

serialization_time, deserialization_time = test(serialize, deserialize)
send_answer("xml", f'xml testing time: {serialization_time}, {deserialization_time}\n')
