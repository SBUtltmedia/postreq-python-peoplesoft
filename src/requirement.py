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
        return "&"
    elif requirement.operator == "OR":
        return "|"


def sift(requirements):
    def sift_single(requirement):
        if requirement.line_type == "CRSE":
            return rqs[0].course_id
        else:
            if requirement.line_type == "RQ":
                sifted_reqs.append("CLAWS")

    sifted_reqs = {}
    rq_groups = frozenset(map(lambda r: r.rq_group, requirements))
    for rq_group in rq_groups:
        rqs = list(filter(lambda r: r.rq_group == rq_group, requirements))
        if len(rqs) == 1:
            sifted_reqs[rq_group] = sift_single(rqs[0])
        else:
            pieces = map(sift_single, rqs)
            operators = map(map_operator, rqs[:1])
            parens = map(lambda r: r.parenth, rqs)
    return list(filter(None, sifted_reqs))

