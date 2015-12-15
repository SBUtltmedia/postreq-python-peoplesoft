from src.csv_reader import read_courses, read_requirements
from src.requirement import sift
import json
#import cProfile


def get_requirement(requirements, course):
    if course.rq_group is not None:
        if course.rq_group in requirements:
            return requirements[course.rq_group]
    return ""


def match_requirements_to_course(requirements, course):
    return {
        "course_id": course.course_id,
        "name": str(course),
        "requirements": get_requirement(requirements, course)
    }


def match_requirements_to_courses(requirements, courses):
    return tuple(map(lambda c: match_requirements_to_course(requirements, c), courses))


def replace_course_ids_with_catalog_numbers(requirements, courses):
    def f(r):
        for course in courses:
            if course.course_id in r:
                r = r.replace(course.course_id, str(course))
        return r
    return {group: f(reqs) for group, reqs in requirements.items()}


def main():
    courses = read_courses()
    requirements = read_requirements()
    sifted_requirements = sift(requirements)
    readable_requirements = replace_course_ids_with_catalog_numbers(sifted_requirements, courses)
    courses_with_requirements = match_requirements_to_courses(readable_requirements, courses)

    with open('output.json', 'w') as outfile:
        json.dump(courses_with_requirements, outfile)


#cProfile.run('main()')
main()
