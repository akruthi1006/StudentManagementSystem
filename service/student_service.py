from model.student import Student

class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, marks):
        if self.find_student(roll_no):
            raise ValueError(f"Student with roll '{roll_no}' already exists.")
        student = Student(roll_no, name, marks)
        self.students.append(student)
        return student

    def view_students(self):
        return list(self.students)

    def find_student(self, roll_no):
        for s in self.students:
            if s.roll_no == str(roll_no):
                return s
        return None

    def delete_student(self, roll_no):
        s = self.find_student(roll_no)
        if s:
            self.students.remove(s)
            return True
        return False
