class Student:
    total_students = 0

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def display(self):
        print("----------------------------")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", Student.calculate_grade(self.marks))
        print("----------------------------")

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
        else:
            return "Fail"

    @classmethod
    def get_total_students(cls):
        return cls.total_students