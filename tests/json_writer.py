import unittest
from src.json_writer import output
from collections import OrderedDict


class JsonWriterTestCase(unittest.TestCase):
    def test_output(self):
        data = OrderedDict()
        data['one'] = 1
        data['two'] = 2
        data['three'] = 3
        expected = "{\"one\": 1, \"two\": 2, \"three\": 3}"
        self.assertEqual(expected, output(data))


if __name__ == '__main__':
    unittest.main()
