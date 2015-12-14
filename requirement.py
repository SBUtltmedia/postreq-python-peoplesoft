class Requirement:
    def __init__(self, rq_group, line_type, rqs_typ, rqrmnt, cond_code, operator, value, course_id, conn, parenth):
        self.rq_group = rq_group
        self.line_type = line_type
        self.rqs_typ = rqs_typ
        self.rqrmnt = rqrmnt
        self.cond_code = cond_code
        self.operator = operator
        self.value = value
        self.course_id = course_id
        self.conn = conn
        self.parenth = parenth
