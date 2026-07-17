

from student import Student


def menu():

    while True:

        print("""
========== Student Management System ==========
1. Add Student
2. View Students
3. Search Student
4. Update Marks
5. Delete Student
6. Show Topper
7. Exit
===============================================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            Student.add_student()

        elif choice == "2":
            Student.view_students()

        elif choice == "3":
            Student.search_student()

        elif choice == "4":
            Student.update_marks()

        elif choice == "5":
            Student.delete_student()

        elif choice == "6":
            Student.topper()

        elif choice == "7":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()