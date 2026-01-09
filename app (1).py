import streamlit as st

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = {}

st.title("📚 Student Attendance Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "Mark Attendance", "View Report", "Low Attendance"]
)

# ---- Add Student ----
if menu == "Add Student":
    st.header("Add Student")
    name = st.text_input("Enter student name")

    if st.button("Add"):
        if name:
            if name not in st.session_state.students:
                st.session_state.students[name] = []
                st.success("Student added")
            else:
                st.warning("Student already exists")
        else:
            st.error("Please enter a name")

# ---- Mark Attendance ----
elif menu == "Mark Attendance":
    st.header("Mark Attendance")

    if st.session_state.students:
        name = st.selectbox("Select student", st.session_state.students.keys())
        status = st.radio("Attendance", ["Present", "Absent"])

        if st.button("Mark"):
            st.session_state.students[name].append("p" if status == "Present" else "a")
            st.success("Attendance marked")
    else:
        st.info("No students added yet")

# ---- Attendance Report ----
elif menu == "View Report":
    st.header("Attendance Report")

    if st.session_state.students:
        for name, record in st.session_state.students.items():
            total = len(record)
            present = record.count("p")
            percent = (present / total * 100) if total > 0 else 0
            st.write(f"**{name}** : {percent:.2f}%")
    else:
        st.info("No data available")

# ---- Low Attendance ----
elif menu == "Low Attendance":
    st.header("Students with Attendance Below 75%")

    found = False
    for name, record in st.session_state.students.items():
        if record:
            percent = record.count("p") / len(record) * 100
            if percent < 75:
                st.write(name)
                found = True

    if not found:
        st.success("No students below 75% attendance")