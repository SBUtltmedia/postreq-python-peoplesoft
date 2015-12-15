import unittest
from src.requirement import Requirement, sift


class MyTestCase(unittest.TestCase):
    def test_one_course(self):
        requirements = (
            Requirement(rq_group="123", key="1", line_type="CRSE", rqs_typ="PRE", course_id="123456", operator="EQ"),
        )
        self.assertEqual({"123": "123456"}, sift(requirements))

    def test_two_courses(self):
        requirements = (
            Requirement(rq_group="123", key="1", line_type="CRSE", rqs_typ="PRE", course_id="123456", operator="EQ"),
            Requirement(rq_group="123", key="2", line_type="CRSE", rqs_typ="PRE", course_id="789012", operator="EQ", conn="AND"),
        )
        self.assertEqual({"123": "123456 & 789012"}, sift(requirements))

    def test_course_and_group(self):
        requirements = (
            Requirement(rq_group="123", key="2", line_type="RQ", rqs_typ="PRE", operator="EQ", conn="AND", rqrmnt="456"),
            Requirement(rq_group="123", key="1", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="123456"),
            Requirement(rq_group="456", key="1", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="444444")
        )
        self.assertEqual({"123": "123456 & 444444", "456": "444444"}, sift(requirements))

    def test_condition(self):
        requirements = (
            Requirement(rq_group="123", key="1", line_type="COND", cond_code="LVL", value="U4", operator="EQ"),
        )
        self.assertEqual({"123": "U4"}, sift(requirements))

    def test_parens(self):
        requirements = (
            Requirement(rq_group="34", key="1", line_type="COND", value="AMR2MAJ", operator="EQ", parenth="("),
            Requirement(rq_group="34", key="2", line_type="COND", value="AMRBA", operator="EQ", conn="OR", parenth=")"),
            Requirement(rq_group="34", key="3", line_type="COND", value="U4", operator="EQ", conn="AND"),
        )
        self.assertEqual({"34": "(AMR2MAJ | AMRBA) & U4"}, sift(requirements))

    '''
    def test_complex_expr(self):
        requirements = (
            Requirement(rq_group="123", key="1", line_type="RQ", rqs_typ="PRE", operator="EQ", rqrmnt="789"),
            Requirement(rq_group="123", key="2", line_type="CRSE", rqs_typ="PRE", operator="EQ", conn="OR", parenth="(", course_id="123456"),
            Requirement(rq_group="123", key="3", line_type="RQ", rqs_typ="PRE", operator="EQ", conn="AND", parenth=")", rqrmnt="456"),
            Requirement(rq_group="456", key="1", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="444444"),
            Requirement(rq_group="789", key="1", line_type="CRSE", rqs_typ="PRE", operator="EQ", course_id="555555")
        )
        self.assertEqual({"123": "555555 | (123456 & 444444)", "456": "444444", "789": "555555"}, sift(requirements))
    '''
    
if __name__ == '__main__':
    unittest.main()
