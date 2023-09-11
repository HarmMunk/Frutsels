from unittest.mock import MagicMock, patch
import json
import unittest

i = 1
new_mock = json.dumps(i)
# print(new_mock)
mock = MagicMock()

# print(json, json.__dict__)
json = mock
# print(json)

new_mock = json.dumps()
# print(mock)
# print(new_mock)


mock=MagicMock(name="RPM")
mock.configure_mock(name="Real Python Mock")
# print(mock.__dict__)

mock = MagicMock(**{"json.return_value": "HELLO"})
# print(mock.__dict__)
# print(mock.json())


def my_function():
    local_variable = 1
    return local_variable


print(my_function.__dict__)


class Testmy_function(unittest.TestCase):
    @patch.object(my_function, "local_variable", 2)
    def test_my_function(self):
        assert my_function() == 2
