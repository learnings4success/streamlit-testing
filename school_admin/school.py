from student import Student
from teacher import Teacher
from db_connection import SchoolDB

class School:
    def __init__(self, school_db: SchoolDB):
        self.db = school_db
        
    def add_student(self, student: Student):
        self.db.insert_student(student)

    def add_teacher(self, teacher: Teacher):
        self.db.insert_teacher(teacher)

    def delete_teacher(self, employee_id):
        return self.db.delete_teacher_db(employee_id)

    def delete_student(self, roll_no):
        return self.db.delete_student_db(roll_no)

    def get_all_students(self):
        rows = self.db.get_all_students()
        return [Student(r["name"], r.get("age"), r.get("address"), r.get("phone_number"), r.get("class_"), r.get("roll_no"), r.get("subjects")) for r in rows]

    def get_all_teachers(self):
        rows = self.db.get_all_teachers()
        return [Teacher(r["name"], r.get("age"), r.get("address"), r.get("phone_number"), r.get("employee_id"), r.get("subjects"), r.get("classes")) for r in rows]