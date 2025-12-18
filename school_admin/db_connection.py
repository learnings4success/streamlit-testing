import sqlite3
# Remove imports of Student and Teacher from db_connection.py
# This avoids circular imports and keeps the DB layer independent.
# from student import Student  <-- REMOVE
# from teacher import Teacher  <-- REMOVE
# from school import School    <-- REMOVE

class SchoolDB:
    def __init__(self, db_path: str = "school.db"):
        # FIX: Add check_same_thread=False to allow Streamlit to share the connection across threads
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        # Keep row_factory if you want dictionary-like access
        self.conn.row_factory = sqlite3.Row 
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor() # Get a cursor for table creation
        
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
        self.conn.commit() # Commit changes after creating tables

    def get_connection(self) -> sqlite3.Connection:
        # This method is less critical if check_same_thread=False is used,
        # but it's good to have for clarity.
        return self.conn
    
    def close_connection(self) -> None:
        self.conn.close()

    def insert_student(self, student):
        # Get a cursor specific to this operation
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
                student.class_, # Assuming student.class_ exists and maps to 'grade' in DB
                student.address,
                student.phone_number,
                student.subjects,
                getattr(student, "attendance", False), # Handle if attendance is not set
            ),
        )
        self.conn.commit()

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
                getattr(teacher, "attendance", False), # Handle if attendance is not set
            ),
        )
        self.conn.commit()

    def get_all_students(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        
        # Convert rows to list of dictionaries (easier for Streamlit's dataframe)
        result = [] 
        for r in rows:
            # Access data by column name thanks to row_factory
            result.append({
                "roll_no": r["roll_no"],
                "name": r["name"],
                "age": r["age"],
                "class_": r["grade"], # Mapping 'grade' from DB to 'class_'
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
        # Return True if a row was actually deleted
        return cur.rowcount > 0

    def delete_teacher_db(self, employee_id) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM teachers WHERE employee_id = ?", (employee_id,))
        self.conn.commit()
        return cur.rowcount > 0