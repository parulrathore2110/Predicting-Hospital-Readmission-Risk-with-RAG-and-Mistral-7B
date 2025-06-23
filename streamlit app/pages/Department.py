import streamlit as st


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if st.button("⌂ Home"):
        st.switch_page("Home.py")

# Sample department data
departments = {
    'Cardiology': {'total_patients': 120, 'avg_readmission_rate': 5.2, 'patients': ['John Doe', 'Alice', 'Bob', 'Charlie']},
    'Neurology': {'total_patients': 85, 'avg_readmission_rate': 4.8, 'patients': ['Jane Smith', 'David', 'Eva', 'Frank']},
    'Oncology': {'total_patients': 95, 'avg_readmission_rate': 6.1, 'patients': ['Grace', 'Hannah', 'Ian']},
    'Orthopedics': {'total_patients': 110, 'avg_readmission_rate': 3.9, 'patients': ['Jack', 'Karen', 'Leo']},
    'Pediatrics': {'total_patients': 75, 'avg_readmission_rate': 2.5, 'patients': ['Mia', 'Noah', 'Olivia']}
}

col1, col2,col3 = st.columns([1, 3, 1])
# Page title
with col1:
     st.title("Departments")

# Search bar at the center

with col3:
     search_query = st.text_input("", placeholder="Search here...", key="search", help="Type and press Enter")
# Layout for department buttons
col1, col2, col3, col4, col5 = st.columns(5)

# Dictionary to map columns to departments
col_dept_map = {
    col1: 'Cardiology',
    col2: 'Neurology',
    col3: 'Oncology',
    col4: 'Orthopedics',
    col5: 'Pediatrics'
}

# Display buttons
for col, dept in col_dept_map.items():
    if col.button(dept):
        st.session_state['selected_department'] = dept
if 'selected_department' not in st.session_state:
    st.session_state['selected_department'] = None
    st.warning("Please select a department to view details.")


# Display department details if a department is selected
if 'selected_department' in st.session_state and st.session_state['selected_department']:
    dept = st.session_state.selected_department
    st.header(f"{dept} Department")
    st.button("Rerun Readmission Risk Analysis")
    st.metric(label="Total Patients", value=departments[dept]['total_patients'])
    st.metric(label="Average Readmission Rate (%)", value=departments[dept]['avg_readmission_rate'])

    st.subheader("Patients List")
    selected_patient = st.selectbox("Select a patient", departments[dept]['patients'])
    if st.button("View Patient Details"):
        st.session_state['selected_patient'] = selected_patient
        st.switch_page("pages/Patient_Data.py")
