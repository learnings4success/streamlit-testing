from user import User

class Teacher(User):
    def __init__(self, name, age, address, phone_number, employee_id, subjects, classes):
        super().__init__(name, age, address, phone_number)
        self.employee_id = employee_id
        self.subjects = subjects
        self.classes = classes
        self.attendance = False

    def set_attendance(self, attendance: bool):
        self.attendance = bool(attendance)

    def __str__(self) -> str:
        attendance = "Present" if self.attendance else "Absent"
        return (
            f"\n\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Subjects: {self.subjects}\n"
            f"Classes: {self.classes}\n"
            f"Address: {self.address}\n"
            f"Phone: {self.phone_number}\n"
            f"Attendance: {attendance}"
        )