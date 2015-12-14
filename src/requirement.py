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


def map_operator(requirement):
    if requirement.operator == "AND":
        return " & "
    elif requirement.operator == "OR":
        return " | "
    else:
        return ""


def sift_single(all_requirements, requirement):
    if requirement.line_type == "CRSE":
        return requirement.course_id
    else:
        if requirement.line_type == "RQ":
            return "CLAWS"


def sift_multiple(all_requirements, requirements):
    pieces = tuple(map(lambda r: sift_rq_group(all_requirements, (r,)), requirements))
    operators = tuple(map(map_operator, requirements))
    parens = tuple(map(lambda r: r.parenth, requirements))
    string = "("
    for i, piece in enumerate(pieces):
        if parens[i] == "(":
            string += "("
        string += operators[i]
        string += piece
        if parens[i] == ")":
            string += ")"
    return string + ")"


def sift_rq_group(all_requirements, rqs):
    if len(rqs) == 1:
        return sift_single(all_requirements, rqs[0])
    else:
        return sift_multiple(all_requirements, rqs)


def sift(requirements):
    sifted_reqs = {}
    rq_groups = frozenset(map(lambda r: r.rq_group, requirements))
    for group in rq_groups:
        rqs = tuple(filter(lambda r: r.rq_group == group, requirements))
        sifted_reqs[group] = sift_rq_group(requirements, rqs)
    return sifted_reqs

