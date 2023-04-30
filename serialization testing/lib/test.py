class TestStruct:
    list_: list[int]
    dict_: dict[str, str]

    def __init__(self, list: list, dict: dict[str, str]) -> None:
        self.list_ = list
        self.dict_ = dict

a = [1, 2, 3]
d = {"a": 1, "b": 2}
test_struct = TestStruct(a, d)