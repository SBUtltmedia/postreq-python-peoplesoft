import csv
from course import Course


class CourseOfferings:
    FILE = 'data/TLT_COURSE_OFFERINGS.csv'

    class Column:
        COURSE_ID = 0
        SUBJECT = 5
        CATALOG = 6


class ReqGroupDetails:
    FILE = 'data/TLT_REQ_GROUP_DETAIL_TABLE.csv'

    class Column:
        RQ_GROUP = 0
        LINE_TYPE = 4
        RQS_TYP = 7
        RQRMNT = 8
        COND_CODE = 9
        OPERATOR = 10
        VALUE = 11
        COURSE_ID = 17
        CONN = 32
        PARENTH = 33


courses = []
with open(CourseOfferings.FILE, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for line in reader:
        courses.append(Course(
            course_id=line[CourseOfferings.Column.COURSE_ID],
            subject=line[CourseOfferings.Column.SUBJECT],
            catalog=line[CourseOfferings.Column.CATALOG]
        ))

print(courses)