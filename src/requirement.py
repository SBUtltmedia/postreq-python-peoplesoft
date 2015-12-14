from src.utils import trim


class Requirement:
    def __init__(self, rq_group, line_type, rqs_typ=None, rqrmnt=None, cond_code=None, operator=None, value=None,
                 ptrn_type=None, course_id=None, conn=None, parenth=None):
        self.rq_group = trim(rq_group)
        self.line_type = trim(line_type)
        self.rqs_typ = trim(rqs_typ)
        self.rqrmnt = trim(rqrmnt)
        self.cond_code = trim(cond_code)
        self.operator = trim(operator)
        self.value = trim(value)
        self.ptrn_type = trim(ptrn_type)
        self.course_id = trim(course_id)
        self.conn = trim(conn)
        self.parenth = trim(parenth)


def map_conn(requirement):
    if requirement.conn == "AND":
        return " & "
    elif requirement.conn == "OR":
        return " | "
    else:
        return ""


def sift_single(all_requirements, requirement):
    if requirement.line_type == "CRSE":
        return requirement.course_id
    if requirement.line_type == "RQ":
        return sift_rq_group(all_requirements, requirement.rqrmnt)
    if requirement.line_type == "COND":
        return None
    if requirement.line_type == "CRSW":
        return None


def sift_multiple(all_requirements, requirements):
    pieces = tuple(map(lambda r: sift_single(all_requirements, r), requirements))
    conns = tuple(map(map_conn, requirements))
    parens = tuple(map(lambda r: r.parenth, requirements))
    string = "("
    for i, piece in enumerate(pieces):
        if parens[i] == "(":
            string += "("
        string += conns[i]
        string += piece
        if parens[i] == ")":
            string += ")"
    return string + ")"


def sift_rq_group(all_requirements, group):
    rqs = tuple(filter(lambda r: r.rq_group == group, all_requirements))
    if len(rqs) == 1:
        return sift_single(all_requirements, rqs[0])
    else:
        return sift_multiple(all_requirements, rqs)


def sift(requirements):
    sifted_reqs = {}
    rq_groups = frozenset(map(lambda r: r.rq_group, requirements))
    for group in rq_groups:
        reqs = sift_rq_group(requirements, group)
        if reqs:
            sifted_reqs[group] = reqs
    return sifted_reqs

