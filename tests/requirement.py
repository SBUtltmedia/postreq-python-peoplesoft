import unittest
from src.requirement import Requirement, sift


class MyTestCase(unittest.TestCase):
    def test_one_course(self):
        requirements = (
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="123456", operator="EQ"),
        )
        self.assertEqual({"123": "123456"}, sift(requirements))

    def test_two_courses(self):
        requirements = (
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="123456", operator="EQ"),
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", course_id="789012", operator="EQ", conn="AND"),
        )
        self.assertEqual({"123": "(123456 & 789012)"}, sift(requirements))

    def test_course_and_group(self):
        requirements = (
            Requirement(rq_group="123", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="123456"),
            Requirement(rq_group="123", line_type="RQ", rqs_typ="PRE", operator="EQ", conn="AND", rqrmnt="456"),
            Requirement(rq_group="456", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="444444")
        )
        self.assertEqual({"123": "(123456 & 444444)"}, sift(requirements))
if __name__ == '__main__':
    unittest.main()
