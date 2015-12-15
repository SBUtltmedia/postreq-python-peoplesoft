from src.csv_reader import read_courses, read_requirements
from src.json_writer import write_pretty, write_minified
from src.requirement import sift
#import cProfile


def get_course_reqs(requirements, course):
    if course.rq_group is not None:
        if course.rq_group in requirements:
            return requirements[course.rq_group]
    return ""


def match_reqs_to_course(requirements, course):
    return {
        "id": course.course_id,
        "course": str(course),
        "reqs": get_course_reqs(requirements, course)
    }


def match_reqs_to_courses(requirements, courses):
    return tuple(map(lambda c: match_reqs_to_course(requirements, c), courses))


def replace_course_ids_with_names(requirements, courses):
    def f(r):
        for course in courses:
            if course.course_id in r:
                r = r.replace(course.course_id, str(course))
        return r
    return {group: f(reqs) for group, reqs in requirements.items()}


def main():
    courses = read_courses()
    reqs = read_requirements()
    sifted_reqs = sift(reqs)
    readable_reqs = replace_course_ids_with_names(sifted_reqs, courses)
    courses_with_reqs = match_reqs_to_courses(readable_reqs, courses)
    sorted_courses_with_reqs = sorted(courses_with_reqs, key=lambda c: c['course'])
    write_pretty(sorted_courses_with_reqs, 'output/requirements.json')
    write_minified(sorted_courses_with_reqs, 'output/requirements.min.json')

#cProfile.run('main()')
main()
