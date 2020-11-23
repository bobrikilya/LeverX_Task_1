class Distribution:
    """Important class that iterates all rooms and students and populates them"""

    def __init__(self, rooms_info, students_info):
        self.rooms_info = rooms_info
        self.students_info = students_info

    def student_distribution(self):
        for room in self.rooms_info:
            room['students'] = []
        for student in self.students_info:
            self.rooms_info[student['room']]['students'].append(student['name'])
        return self.rooms_info


