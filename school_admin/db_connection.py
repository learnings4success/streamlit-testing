from student import Student
from teacher import Teacher
from school import School
from db_connection import SchoolDB
import os

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def display():
    print("*"*50)
    print("Press 1 for add the student.")
    print("Press 2 for add the teacher.")
    print("Press 3 for delete the student.")
    print("Press 4 for delete the teacher.")
    print("Press 5 get all students.")
    print("Press 6 get all teachers.")
    print("Press q for close the software.\n")
    print("*"*50)

schooldb = SchoolDB("school_database.db")
school = School(schooldb)

def enter_user_details():
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    phone_number = input("Phone No.: ")
    return {
        "name": name,
        "age": age,
        "address": address,
        "phone_number": phone_number,
    }
while True:
    clear_screen()
    display()
    value = input("Enter your input: ").strip().lower()
    match value:
        case '1':
            print("Enter the student's details:")
            data = enter_user_details()
            class_ = input("Class: ")
            roll_no = input("Roll no: ")
            subjects = input("Subjects (comma separated): ")
            student = Student(data['name'], data['age'], data['address'], data['phone_number'], class_, roll_no, subjects)
            school.add_student(student)
            print(f"Added student {student.name} (roll {student.roll_no})")
            input("Press Enter to continue...")
        case '2':
            print("Enter the teacher's details:")
            data = enter_user_details()
            employee_id = input("Employee ID: ")
            subjects = input("Subjects (comma separated): ")
            classes = input("Classes (comma separated): ")
            teacher = Teacher(data['name'], data['age'], data['address'], data['phone_number'], employee_id, subjects, classes)
            school.add_teacher(teacher)
            print(f"Added teacher {teacher.name} (id {teacher.employee_id})")
            input("Press Enter to continue...")
        case '3':
            roll_no = input("Roll no to delete: ")
            removed = school.delete_student(roll_no)
            if removed:
                print(f"Deleted student with roll {roll_no}")
            else:
                print(f"No student found with roll {roll_no}")
            input("Press Enter to continue...")
        case '4':
            employee_id = input("Employee id to delete: ")
            removed = school.delete_teacher(employee_id)
            if removed:
                print(f"Deleted teacher with id {employee_id}")
            else:
                print(f"No teacher found with id {employee_id}")
            input("Press Enter to continue...")
        case '5':
            print("Students:")
            for s in school.get_all_students():
                print(s)
            input("Press Enter to continue...")
        case '6':
            print("Teachers:")
            for t in school.get_all_teachers():
                print(t)
            input("Press Enter to continue...")
        case 'q' | 'quit' | 'exit':
            print("Exiting...")
            break
        case _:
            print("Unrecognized option. Please try again.")