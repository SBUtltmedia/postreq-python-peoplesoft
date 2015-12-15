from src.utils import trim, trim_leading_zeroes
from src.settings import AND, OR


class Requirement:
    def __init__(self, rq_group, line, line_type, rqs_typ=None, rqrmnt=None, cond_code=None, operator=None, value=None,
                 acad_group=None, subject=None, catalog=None, ptrn_type=None, course_id=None, designation=None,
                 conn=None, parenth=None):
        self.rq_group = trim_leading_zeroes(trim(rq_group))
        self.line = trim(line)
        self.line_type = trim(line_type)
        self.rqs_typ = trim(rqs_typ)
        self.rqrmnt = trim(rqrmnt)
        self.cond_code = trim(cond_code)
        self.operator = trim(operator)
        self.value = trim(value)
        self.acad_group = trim(acad_group)
        self.subject = trim(subject)
        self.catalog = trim(catalog)
        self.ptrn_type = trim(ptrn_type)
        self.course_id = trim(course_id)
        self.designation = trim(designation)
        self.conn = trim(conn)
        self.parenth = trim(parenth)


def map_conn(requirement):
    if requirement.conn == "AND":
        return " %s " % AND
    elif requirement.conn == "OR":
        return " %s " % OR
    else:
        return ""


def sift_single(all_requirements, requirement):
    if requirement.line_type == "CRSE":
        return requirement.course_id
    if requirement.line_type == "RQ":
        return sift_rq_group(all_requirements, requirement.rqrmnt)
    if requirement.line_type == "COND":
        if requirement.value is not None:
            return requirement.value
    if requirement.line_type == "CRSW":
        if requirement.designation is not None:
            return requirement.designation
        elif requirement.subject is not None:
            return requirement.subject + " " + (requirement.catalog if requirement.catalog is not None else "")
        elif requirement.acad_group is not None:
            if requirement.catalog is not None:
                return requirement.acad_group + " " + requirement.catalog
            elif requirement.subject is not None:
                return requirement.acad_group + " " + requirement.subject
    #raise Exception("Requirement " + requirement.rq_group)
    return requirement.cond_code


def sift_multiple(all_requirements, requirements):
    pieces = tuple(map(lambda r: sift_single(all_requirements, r), requirements))
    conns = tuple(map(map_conn, requirements))
    parens = tuple(map(lambda r: r.parenth, requirements))
    string = ""
    for i, piece in enumerate(pieces):
        if piece:
            string += conns[i]
            string += "(" if parens[i] == "(" else ""
            string += piece
            string += ")" if parens[i] == ")" else ""
    return string


def sift_rq_group(all_requirements, group):
    rqs = tuple(filter(lambda r: r.rq_group == group, all_requirements))
    rqs = sorted(rqs, key=lambda rq: int(rq.line))
    if len(rqs) == 1:
        return sift_single(all_requirements, rqs[0])
    else:
        return sift_multiple(all_requirements, rqs)


def sift_reqs(requirements):
    sifted_reqs = {}
    rq_groups = frozenset(map(lambda r: r.rq_group, requirements))
    for group in rq_groups:
        sifted_reqs[group] = sift_rq_group(requirements, group)
    return sifted_reqs

