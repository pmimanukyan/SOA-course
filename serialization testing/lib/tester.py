import timeit

def test(serialize, deserialize):
    starttime = timeit.default_timer()
    serialized = serialize()
    serialization_time = timeit.default_timer() - starttime

    starttime = timeit.default_timer()
    deserialized = deserialize(serialized)
    deserialization_time = timeit.default_timer() - starttime

    return serialization_time, deserialization_time