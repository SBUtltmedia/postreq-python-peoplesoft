from src.csv_reader import read_courses, read_requirements
from src.json_writer import write_pretty, write_minified
from src.requirement import sift_reqs, get_coreqs, get_prereqs
from src.course import group_courses, ungroup_courses
from collections import OrderedDict
#import cProfile


def create_course_object(course, prereqs, coreqs):
    d = OrderedDict()
    d['id'] = course.course_id
    d['course'] = str(course)
    d['prereqs'] = course.find_reqs(prereqs)
    d['coreqs'] = course.find_reqs(coreqs)
    return d


def match_reqs_to_courses(prereqs, coreqs, courses):
    return tuple(map(lambda c: create_course_object(c, prereqs, coreqs), courses))


def replace_course_ids_with_names(requirements, courses):
    def f(r):
        for course in courses:
            if course.course_id in r:
                r = r.replace(course.course_id, str(course))
        return r
    return {group: f(reqs) for group, reqs in requirements.items()}


def main():
    reqs = read_requirements()
    prereqs = get_prereqs(reqs)
    coreqs = get_coreqs(reqs)
    courses = read_courses()
    sifted_prereqs = sift_reqs(prereqs)
    sifted_coreqs = sift_reqs(coreqs)
    grouped_courses = group_courses(courses)
    readable_prereqs = replace_course_ids_with_names(sifted_prereqs, grouped_courses)
    readable_coreqs = replace_course_ids_with_names(sifted_coreqs, grouped_courses)
    courses_with_reqs = match_reqs_to_courses(readable_prereqs, readable_coreqs, courses)
    ungrouped_courses_with_reqs = ungroup_courses(courses_with_reqs)
    sorted_courses_with_reqs = sorted(ungrouped_courses_with_reqs, key=lambda c: c['course'])
    write_pretty(sorted_courses_with_reqs, 'output/requirements.json')
    write_minified(sorted_courses_with_reqs, 'output/requirements.min.json')

#cProfile.run('main()')
main()
