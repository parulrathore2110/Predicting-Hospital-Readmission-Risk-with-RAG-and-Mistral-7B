import streamlit as st

if st.button("⌂ Home"):
        st.switch_page("Home.py")
        
# Define Department and Disease Data
department_diseases = {
    'Cardiology': ['Hypertension', 'Arrhythmia', 'Heart Failure'],
    'Neurology': ['Stroke', 'Epilepsy', 'Migraine'],
    'Oncology': ['Lung Cancer', 'Breast Cancer', 'Leukemia'],
    'Orthopedics': ['Fracture', 'Arthritis', 'Osteoporosis']
}

# Initialize Session State
if 'comorbidities' not in st.session_state:
    st.session_state.comorbidities = False
if 'selected_departments' not in st.session_state:
    st.session_state.selected_departments = []
if 'selected_diseases' not in st.session_state:
    st.session_state.selected_diseases = []

# Callback Function for Form Submission
def submit_form():
    st.session_state.submitted = True

# Form Layout
with st.form(key='new_patient_form'):
    st.header("New Patient Entry")

    # First and Last Name
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        last_name = st.text_input("Last Name")

    # Age and Gender
    col3, col4 = st.columns(2)
    with col3:
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
    with col4:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    # Diagnosis Section
    st.subheader("Diagnosis")

    # Comorbidities Checkbox
    comorbidities = st.checkbox("Comorbidities", value=st.session_state.comorbidities)

    if comorbidities:
        # Multi-select for Departments
        selected_departments = st.multiselect(
            "Select Departments",
            list(department_diseases.keys()),
            default=st.session_state.selected_departments
        )

        # Multi-select for Diseases
        selected_diseases = []
        for dept in selected_departments:
            diseases = st.multiselect(
                f"Select Diseases in {dept}",
                department_diseases[dept],
                default=[d for d in st.session_state.selected_diseases if d in department_diseases[dept]]
            )
            selected_diseases.extend(diseases)
        st.session_state.selected_departments = selected_departments
        st.session_state.selected_diseases = selected_diseases
    else:
        # Single Department Selection
        selected_department = st.selectbox(
            "Select Department",
            list(department_diseases.keys())
        )

        # Diseases Dropdown
        selected_disease = st.selectbox(
            "Select Disease",
            department_diseases[selected_department]
        )
        st.session_state.selected_departments = [selected_department]
        st.session_state.selected_diseases = [selected_disease]

    # Vitals and Other Patient Data
    st.subheader("Vitals and Patient Data")
    temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, step=0.1)
    blood_pressure = st.text_input("Blood Pressure (mmHg)")
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, step=1)
    oxygen_saturation = st.number_input("Oxygen Saturation (%)", min_value=50, max_value=100, step=1)

    # Description Box
    st.subheader("Description")
    description = st.text_area("Describe the patient's condition and other details.")

    # Submit Button
    submit_button = st.form_submit_button(label='Submit', on_click=submit_form)

# Process the form data after submission
if 'submitted' in st.session_state and st.session_state.submitted:
    st.success("Patient data submitted successfully!")
    # Here, you can add code to save the data to a database or perform other actions
    st.session_state.submitted = False  # Reset the submission state
