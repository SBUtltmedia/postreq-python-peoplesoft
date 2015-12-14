class Requirement:
    def __init__(self, rq_group, line_type, rqs_typ=None, rqrmnt=None, cond_code=None, operator=None, value=None,
                 ptrn_type=None, course_id=None, conn=None, parenth=None):
        self.rq_group = rq_group
        self.line_type = line_type
        self.rqs_typ = rqs_typ
        self.rqrmnt = rqrmnt
        self.cond_code = cond_code
        self.operator = operator
        self.value = value
        self.ptrn_type = ptrn_type
        self.course_id = course_id
        self.conn = conn
        self.parenth = parenth


def sift(requirements):
    sifted_reqs = []
    rq_groups = frozenset(map(lambda r: r.rq_group, requirements))
    for rq_group in rq_groups:
        rqs = list(filter(lambda r: r.rq_group == rq_group, requirements))
        if len(rqs) == 1:
            if rqs[0].line_type == "CRSE":
                if rqs[0].ptrn_type == "SMPL":
                    sifted_reqs.append("BOG")
                else:
                    sifted_reqs.append(rqs[0].course_id)
            else:
                if rqs[0].line_type == "RQ":
                    sifted_reqs.append("CLAWS")
    return sifted_reqs

