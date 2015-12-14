class Course:
    def __init__(self, course_id, subject, catalog):
        self.course_id = course_id.strip()
        self.subject = subject.strip()
        self.catalog = catalog.strip()

    def __repr__(self):
        return self.subject + " " + self.catalog
