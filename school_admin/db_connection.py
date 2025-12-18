import sqlite3

# NOTE: I commented these out to prevent Circular Import errors. 
# You don't strictly need them for the logic below to work.
# from student import Student
# from teacher import Teacher

class SchoolDB:
    def __init__(self, db_path: str = "school.db"):
        # --- FIX IS HERE: check_same_thread=False ---
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        
        cur = self.conn.cursor()
        
        # Create Students Table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT,
                address TEXT,
                phone_number TEXT,
                subjects TEXT,
                attendance BOOLEAN DEFAULT 0
            )
        """)

        # Create Teachers Table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                employee_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                address TEXT,
                phone_number TEXT,
                subjects TEXT,
                classes TEXT,
                attendance BOOLEAN DEFAULT 0
            )
        """)
        self.conn.commit()

    def get_connection(self) -> sqlite3.Connection:
        return self.conn
    
    def close_connection(self) -> None:
        self.conn.close()

    # Removed type hint ": Student" to avoid import error
    def insert_student(self, student):
        cur = self.conn.cursor()
        
        cur.execute(
            """
            INSERT OR REPLACE INTO students (roll_no, name, age, grade, address, phone_number, subjects, attendance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student.roll_no,
                student.name,
                student.age,
                student.class_, 
                student.address,
                student.phone_number,
                student.subjects,
                getattr(student, "attendance", False),
            ),
        )
        self.conn.commit()

    # Removed type hint ": Teacher" to avoid import error
    def insert_teacher(self, teacher) -> None:
        cur = self.conn.cursor()
        
        cur.execute(
            """
            INSERT OR REPLACE INTO teachers (employee_id, name, age, address, phone_number, subjects, classes, attendance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                teacher.employee_id,
                teacher.name,
                teacher.age,
                teacher.address,
                teacher.phone_number,
                teacher.subjects,
                teacher.classes,
                getattr(teacher, "attendance", False),
            ),
        )
        self.conn.commit()

    def get_all_students(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        
        result = [] 
        for r in rows:
            result.append({
                "roll_no": r["roll_no"],
                "name": r["name"],
                "age": r["age"],
                "class_": r["grade"],
                "address": r["address"],
                "phone_number": r["phone_number"],
                "subjects": r["subjects"],
                "attendance": bool(r["attendance"]),
            })
        return result

    def get_all_teachers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM teachers")
        rows = cur.fetchall()
        
        result = []
        for r in rows:
            result.append({
                "employee_id": r["employee_id"],
                "name": r["name"],
                "age": r["age"],
                "address": r["address"],
                "phone_number": r["phone_number"],
                "subjects": r["subjects"],
                "classes": r["classes"],
                "attendance": bool(r["attendance"]),
            })
        return result

    def delete_student_db(self, roll_no) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
        self.conn.commit()
        return cur.rowcount > 0

    def delete_teacher_db(self, employee_id) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM teachers WHERE employee_id = ?", (employee_id,))
        self.conn.commit()
        return cur.rowcount > 0