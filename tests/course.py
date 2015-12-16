import unittest
from src.course import Course, CourseGroup, group_courses, ungroup_courses


class CourseTestCase(unittest.TestCase):
    def test_course_grouping(self):
        courses = (
            Course(course_id="111111", subject="ABC", catalog="123", rq_group="518"),
            Course(course_id="111111", subject="DEF", catalog="123", rq_group="518"),
            Course(course_id="222222", subject="XYZ", catalog="456"),
        )
        expected = (
            CourseGroup(course_id="111111", courses=courses[:2]),
            courses[2]
        )
        self.assertTupleEqual(expected, group_courses(courses))

    def test_course_ungrouping(self):
        courses = (
            Course(course_id="111111", subject="ABC", catalog="123", rq_group="518"),
            Course(course_id="111111", subject="DEF", catalog="123", rq_group="518"),
            Course(course_id="222222", subject="XYZ", catalog="456"),
        )
        grouped_courses = (
            CourseGroup(course_id="111111", courses=courses[:2]),
            courses[2]
        )
        self.assertTupleEqual(courses, ungroup_courses(grouped_courses))

if __name__ == '__main__':
    unittest.main()
