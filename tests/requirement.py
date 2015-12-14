import unittest
from src.requirement import Requirement, sift


class MyTestCase(unittest.TestCase):
    def test_something(self):
        requirements = [
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="123456")
        ]
        self.assertEqual(sift(requirements), ["123456"])


if __name__ == '__main__':
    unittest.main()
