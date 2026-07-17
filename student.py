
class Student:
    students = []

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        grade = Student.calculate_grade(self.marks)
        print(f"""
-------------------------
Name      : {self.name}
Roll No   : {self.roll_no}
Marks     : {self.marks}
Grade     : {grade}
-------------------------
""")

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        return "Fail"

    @classmethod
    def add_student(cls):
        roll = input("Enter Roll Number: ")

        for student in cls.students:
            if student.roll_no == roll:
                print("Student already exists.")
                return

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(name, roll, marks)
        cls.students.append(student)

        print("Student Added Successfully!")

    @classmethod
    def view_students(cls):
        if not cls.students:
            print("No Students Found.")
            return

        for student in cls.students:
            student.display()

    @classmethod
    def search_student(cls):
        roll = input("Enter Roll Number: ")

        for student in cls.students:
            if student.roll_no == roll:
                student.display()
                return

        print("Student Not Found.")

    @classmethod
    def update_marks(cls):
        roll = input("Enter Roll Number: ")

        for student in cls.students:
            if student.roll_no == roll:
                student.marks = float(input("Enter New Marks: "))
                print("Marks Updated Successfully.")
                return

        print("Student Not Found.")

    @classmethod
    def delete_student(cls):
        roll = input("Enter Roll Number: ")

        for student in cls.students:
            if student.roll_no == roll:
                cls.students.remove(student)
                print("Student Deleted Successfully.")
                return

        print("Student Not Found.")

    @classmethod
    def topper(cls):
        if not cls.students:
            print("No Students Available.")
            return

        top = max(cls.students, key=lambda x: x.marks)

        print("\nTopper")
        top.display()