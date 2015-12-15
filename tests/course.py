import unittest
from src.course import Course, CourseGroup, group_courses


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
        self.assertEqual(expected, group_courses(courses))


if __name__ == '__main__':
    unittest.main()
