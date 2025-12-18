from user import User

class Student(User):
    def __init__(self, name, age, address, phone_number, class_, roll_no, subjects):
        super().__init__(name, age, address, phone_number)
        self.class_ = class_
        self.roll_no = roll_no
        self.subjects = subjects
        self.attendance = False

    def set_attendance(self, attendance: bool):
        self.attendance = bool(attendance)

    def __str__(self) -> str:
        attendance = "Present" if self.attendance else "Absent"
        return (
            f"\n\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Grade: {self.class_}\n"
            f"Roll: {self.roll_no}\n"
            f"Subjects: {self.subjects}\n"
            f"Address: {self.address}\n"
            f"Phone: {self.phone_number}\n"
            f"Attendance: {attendance}"
        )