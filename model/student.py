class Student:
    def __init__(self, roll_no: str, name: str, marks: float):
        self.roll_no = str(roll_no)
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}"
