import unittest
from src.requirement import Requirement, sift

class MyTestCase(unittest.TestCase):
    def test_one_course(self):
        requirements = (
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="123456"),
        )
        self.assertEqual({"123": "123456"}, sift(requirements))

    def test_two_courses(self):
        requirements = (
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="123456"),
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="789012", operator="AND"),
        )
        self.assertEqual({"123": "(123456 & 789012)"}, sift(requirements))

if __name__ == '__main__':
    unittest.main()
