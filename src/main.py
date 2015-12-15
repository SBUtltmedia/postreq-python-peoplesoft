from src.csv_reader import read_courses, read_requirements
from src.json_writer import write_pretty, write_minified
from src.requirement import sift_reqs
from src.course import group_courses
#import cProfile


def match_reqs_to_course(requirements, course):
    return {
        "id": course.course_id,
        "course": str(course),
        "reqs": course.find_reqs(requirements)
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
    reqs = read_requirements()
    courses = read_courses()
    sifted_reqs = sift_reqs(reqs)
    grouped_courses = group_courses(courses)
    readable_reqs = replace_course_ids_with_names(sifted_reqs, grouped_courses)
    courses_with_reqs = match_reqs_to_courses(readable_reqs, grouped_courses)
    sorted_courses_with_reqs = sorted(courses_with_reqs, key=lambda c: c['course'])
    write_pretty(sorted_courses_with_reqs, 'output/requirements.json')
    write_minified(sorted_courses_with_reqs, 'output/requirements.min.json')

#cProfile.run('main()')
main()
