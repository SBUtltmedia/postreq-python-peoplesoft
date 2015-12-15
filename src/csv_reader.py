import csv
from src.course import Course
from src.requirement import Requirement


class CourseOfferings:
    FILE = 'data/TLT_COURSE_OFFERINGS.csv'

    class Column:
        COURSE_ID = 0
        SUBJECT = 5
        CATALOG = 6
        RQ_GROUP = 16


class ReqGroupDetails:
    FILE = 'data/TLT_REQ_GROUP_DETAIL_TABLE.csv'

    class Column:
        RQ_GROUP = 0
        KEY = 2
        LINE_TYPE = 4
        RQS_TYP = 7
        RQRMNT = 8
        COND_CODE = 9
        OPERATOR = 10
        VALUE = 11
        ACAD_GROUP = 13
        SUBJECT = 14
        CATALOG = 15
        PTRN_TYPE = 16
        COURSE_ID = 17
        DESIGNATION = 31
        CONN = 32
        PARENTH = 33


def read_courses():
    courses = []
    with open(CourseOfferings.FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for line in reader:
            courses.append(Course(
                course_id=line[CourseOfferings.Column.COURSE_ID],
                subject=line[CourseOfferings.Column.SUBJECT],
                catalog=line[CourseOfferings.Column.CATALOG],
                rq_group=line[CourseOfferings.Column.RQ_GROUP]
            ))
    return courses


def read_requirements():
    requirements = []
    with open(ReqGroupDetails.FILE, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for line in reader:
            requirements.append(Requirement(
                rq_group=line[ReqGroupDetails.Column.RQ_GROUP],
                key=line[ReqGroupDetails.Column.KEY],
                line_type=line[ReqGroupDetails.Column.LINE_TYPE],
                rqs_typ=line[ReqGroupDetails.Column.RQS_TYP],
                rqrmnt=line[ReqGroupDetails.Column.RQRMNT],
                cond_code=line[ReqGroupDetails.Column.COND_CODE],
                operator=line[ReqGroupDetails.Column.OPERATOR],
                value=line[ReqGroupDetails.Column.VALUE],
                acad_group=line[ReqGroupDetails.Column.ACAD_GROUP],
                subject=line[ReqGroupDetails.Column.SUBJECT],
                catalog=line[ReqGroupDetails.Column.CATALOG],
                ptrn_type=line[ReqGroupDetails.Column.PTRN_TYPE],
                course_id=line[ReqGroupDetails.Column.COURSE_ID],
                designation=line[ReqGroupDetails.Column.DESIGNATION],
                conn=line[ReqGroupDetails.Column.CONN],
                parenth=line[ReqGroupDetails.Column.PARENTH]
            ))
    return requirements
