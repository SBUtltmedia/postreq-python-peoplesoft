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
        self.rqrmnt = trim_leading_zeroes(trim(rqrmnt))
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


def get_prereqs(requirements):
    return tuple(filter(lambda r: r.rqs_typ == "PRE", requirements))


def get_coreqs(requirements):
    return tuple(filter(lambda r: r.rqs_typ == "CO", requirements))


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
        else:
            return " ".join([(requirement.subject if requirement.subject is not None else ""),
                             (requirement.catalog if requirement.catalog is not None else "###")])
    #raise Exception("Requirement " + requirement.rq_group)
    return requirement.cond_code


def sift_multiple(all_requirements, requirements):
    pieces = [sift_single(all_requirements, r) for r in requirements]
    conns = [map_conn(r) for r in requirements]
    parens = [r.parenth for r in requirements]
    string = ""
    for i, piece in enumerate(pieces):
        if piece:
            string += conns[i]
            string += "(" if parens[i] == "(" else ""
            string += piece
            string += ")" if parens[i] == ")" else ""
    return "(%s)" % string if len(pieces) > 1 else string


def sift_rq_group(all_requirements, group):
    rqs = tuple(filter(lambda r: r.rq_group == group, all_requirements))
    rqs = sorted(rqs, key=lambda rq: int(rq.line))
    if len(rqs) == 1:
        return sift_single(all_requirements, rqs[0])
    else:
        return sift_multiple(all_requirements, rqs)


def sift_reqs(requirements):
    sifted_reqs = {}
    rq_groups = frozenset([r.rq_group for r in requirements])
    for group in rq_groups:
        sifted_reqs[group] = sift_rq_group(requirements, group)
    return sifted_reqs
