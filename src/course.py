from abc import abstractmethod
from src.utils import trim, trim_leading_zeroes
from src.settings import OR


class AbstractCourse:
    @abstractmethod
    def find_reqs(self, requirements):
        raise Exception("Not implmented")


class Course(AbstractCourse):
    def __init__(self, course_id, subject, catalog, rq_group=None):
        self.course_id = trim(course_id)
        self.subject = trim(subject)
        self.catalog = trim(catalog)
        self.rq_group = trim_leading_zeroes(trim(rq_group))

    def find_reqs(self, requirements):
        if self.rq_group is not None:
            if self.rq_group in requirements:
                return requirements[self.rq_group]
        return ""

    def __repr__(self):
        return self.subject + " " + self.catalog

    def __lt__(self, other):
        return str(self) < str(other)


class CourseGroup(AbstractCourse):
    def __init__(self, course_id, courses):
        self.course_id = course_id
        self.courses = courses

    def find_reqs(self, requirements):
        return self.courses[0].find_reqs(requirements)

    def __repr__(self):
        return "(%s)" % (" %s " % OR).join(tuple(map(lambda c: str(c), self.courses)))

    def __eq__(self, other):
        return self.course_id == other.course_id and sorted(self.courses) == sorted(other.courses)


def group_courses(courses):
    grouped_courses = []
    course_ids = sorted(frozenset(map(lambda c: c.course_id, courses)))
    for course_id in course_ids:
        courses_in_group = tuple(filter(lambda c: c.course_id == course_id, courses))
        if len(courses_in_group) == 1:
            grouped_courses.append(courses_in_group[0])
        else:
            grouped_courses.append(CourseGroup(course_id, courses_in_group))
    return tuple(grouped_courses)
