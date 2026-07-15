from student import Student

students = []


def add_student():
    roll_no = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll_no:
            print("Roll Number already exists.")
            return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
        return

    student = Student(roll_no, name, marks)
    students.append(student)

    print("Student Added Successfully.")


def view_students():
    if len(students) == 0:
        print("No Students Found.")
        return

    for student in students:
        student.display()


def search_student():
    roll_no = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll_no:
            student.display()
            return

    print("Student Not Found")


def update_marks():
    roll_no = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll_no:

            marks = float(input("Enter New Marks: "))

            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100.")
                return

            student.marks = marks
            print("Marks Updated Successfully")
            return

    print("Student Not Found")


def delete_student():
    roll_no = int(input("Enter Roll Number: "))

    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            Student.total_students -= 1
            print("Student Deleted Successfully")
            return

    print("Student Not Found")


def show_topper():
    if len(students) == 0:
        print("No Students Found.")
        return

    topper = students[0]

    for student in students:
        if student.marks > topper.marks:
            topper = student

    print("\n***** TOPPER *****")
    topper.display()


def menu():
    while True:

        print(" Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            print("Thank You!")
            print("Total Students:", Student.get_total_students())
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()