from service.student_service import StudentService

class StudentController:
    def __init__(self):
        self.service = StudentService()

    def _input_roll(self, prompt="Enter Roll No: "):
        return input(prompt).strip()

    def _input_name(self, prompt="Enter Name: "):
        return input(prompt).strip()

    def _input_marks(self, prompt="Enter Marks: "):
        while True:
            m = input(prompt).strip()
            try:
                if m == "":
                    return 0.0
                return float(m)
            except ValueError:
                print("Please enter numeric marks (e.g., 75.5)")

    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                roll_no = self._input_roll()
                name = self._input_name()
                marks = self._input_marks()
                try:
                    student = self.service.add_student(roll_no, name, marks)
                    print("✅ Student Added:", student)
                except ValueError as e:
                    print("❌", e)

            elif choice == "2":
                students = self.service.view_students()
                if not students:
                    print("No students found.")
                else:
                    for s in students:
                        print(s)

            elif choice == "3":
                roll_no = self._input_roll("Enter Roll No to search: ")
                student = self.service.find_student(roll_no)
                if student:
                    print("✅ Student Found:", student)
                else:
                    print("❌ Student not found")

            elif choice == "4":
                roll_no = self._input_roll("Enter Roll No to delete: ")
                if self.service.delete_student(roll_no):
                    print("✅ Student Deleted")
                else:
                    print("❌ Student not found")

            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, try again!")
