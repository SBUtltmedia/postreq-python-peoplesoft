from src.csv_reader import read_courses, read_requirements
from src.requirement import sift
import json


def match_requirements_to_courses(requirements, courses):
    pass


def replace_course_ids_with_catalog_numbers(requirements, courses):
    pass


courses = read_courses()
requirements = read_requirements()
sifted_requirements = sift(requirements)
readable_requirements = replace_course_ids_with_catalog_numbers(sifted_requirements)
courses_with_requirements = match_requirements_to_courses(courses, readable_requirements)

with open('output.json', 'w') as outfile:
    json.dump(courses_with_requirements, outfile)

