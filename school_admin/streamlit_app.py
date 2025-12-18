import streamlit as st
import pandas as pd # Optional: Makes tables look pretty

# IMPORT YOUR EXISTING MODULES
# We assume these files are in the same folder
from student import Student
from teacher import Teacher
from school import School
from db_connection import SchoolDB

# --- 1. SETUP & CACHING ---
# In CLI, you init the DB once. In Streamlit, the script re-runs on every click.
# We use @st.cache_resource to make sure we connect to the DB only ONCE.
@st.cache_resource
def get_school_system():
    # This connects to your existing SQLite database
    schooldb = SchoolDB("school_database.db")
    school = School(schooldb)
    return school

school = get_school_system()

st.set_page_config(page_title="School Manager", page_icon="🏫")

# --- 2. SIDEBAR NAVIGATION (Replaces the 'while True' loop) ---
st.sidebar.title("🏫 School Admin")
menu = ["Home", "Add Student", "Add Teacher", "Delete Student", "Delete Teacher", "View Students", "View Teachers"]
choice = st.sidebar.radio("Go to:", menu)

# --- 3. MAIN LOGIC ---

if choice == "Home":
    st.title("Welcome to School Management System")
    st.write("Use the sidebar menu to manage your school records.")
    st.info("Database Connection: Active ✅")

# === ADD STUDENT ===
elif choice == "Add Student":
    st.header("➕ Add New Student")
    
    # We use a FORM so the page doesn't reload after typing every letter
    with st.form("student_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=1, step=1)
            address = st.text_input("Address")
        with col2:
            phone = st.text_input("Phone Number")
            student_class = st.text_input("Class")
            roll_no = st.text_input("Roll No")
        
        subjects = st.text_input("Subjects (comma separated)", "Maths, Punjabi, English")
        
        # The Submit Button
        submitted = st.form_submit_button("Save Student")
        
        if submitted:
            if name and roll_no:
                # Create the object using your existing Class logic
                new_student = Student(name, int(age), address, phone, student_class, roll_no, subjects)
                school.add_student(new_student)
                st.success(f"✅ Student {name} (Roll: {roll_no}) Added Successfully!")
            else:
                st.error("⚠️ Name and Roll No are required!")

# === ADD TEACHER ===
elif choice == "Add Teacher":
    st.header("➕ Add New Teacher")
    
    with st.form("teacher_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=18, step=1)
            address = st.text_input("Address")
        with col2:
            phone = st.text_input("Phone Number")
            emp_id = st.text_input("Employee ID")
        
        subjects = st.text_input("Subjects (comma separated)")
        classes = st.text_input("Classes (comma separated)")
        
        submitted = st.form_submit_button("Save Teacher")
        
        if submitted:
            if name and emp_id:
                new_teacher = Teacher(name, int(age), address, phone, emp_id, subjects, classes)
                school.add_teacher(new_teacher)
                st.success(f"✅ Teacher {name} (ID: {emp_id}) Added Successfully!")
            else:
                st.error("⚠️ Name and Employee ID are required!")

# === DELETE STUDENT ===
elif choice == "Delete Student":
    st.header("🗑️ Delete Student")
    st.warning("Warning: This action cannot be undone.")
    
    roll_to_delete = st.text_input("Enter Roll No to Delete:")
    
    if st.button("Delete Student"):
        # Calling your existing method
        removed = school.delete_student(roll_to_delete)
        if removed:
            st.success(f"Student with Roll No {roll_to_delete} deleted.")
        else:
            st.error("Student not found!")

# === DELETE TEACHER ===
elif choice == "Delete Teacher":
    st.header("🗑️ Delete Teacher")
    
    id_to_delete = st.text_input("Enter Employee ID to Delete:")
    
    if st.button("Delete Teacher"):
        removed = school.delete_teacher(id_to_delete)
        if removed:
            st.success(f"Teacher with ID {id_to_delete} deleted.")
        else:
            st.error("Teacher not found!")

# === VIEW STUDENTS ===
elif choice == "View Students":
    st.header("👨‍🎓 All Students")
    
    # Get list from your backend
    students = school.get_all_students()
    
    if students:
        # Convert objects to a format Streamlit can display nicely
        # Assuming your Student object has a __dict__ or we can extract fields
        student_data = []
        for s in students:
            # We map the object attributes to a dictionary for the table
            student_data.append({
                "Name": s.name,
                "Roll No": s.roll_no,
                "Class": s.class_, # Assuming attribute is named class_
                "Phone": s.phone_number,
                "Subjects": s.subjects
            })
        
        # Display as a pretty interactive table
        st.dataframe(student_data, use_container_width=True)
    else:
        st.info("No students found in database.")

# === VIEW TEACHERS ===
elif choice == "View Teachers":
    st.header("👩‍🏫 All Teachers")
    
    teachers = school.get_all_teachers()
    
    if teachers:
        teacher_data = []
        for t in teachers:
            teacher_data.append({
                "Name": t.name,
                "ID": t.employee_id,
                "Phone": t.phone_number,
                "Subjects": t.subjects,
                "Classes": t.classes_assigned # Assuming attribute name
            })
            
        st.dataframe(teacher_data, use_container_width=True)
    else:
        st.info("No teachers found in database.")