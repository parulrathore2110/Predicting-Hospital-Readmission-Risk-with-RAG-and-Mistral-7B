import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if st.button("⌂ Home"):
        st.switch_page("Home.py")
# Sample patient data
patient_data = {
    'John Doe': {
        'Gender': 'Male',
        'Department': 'Cardiology',
        'Diagnosis': 'Hypertension',
        'Admissions': '2025-03-10 14:30',
        'Medication': 'Lisinopril',
        'Clinical Insights': 'Blood pressure under control.',
        'Discharge Summary': 'Scheduled for follow-up in 2 weeks.'
    },
    'Jane Smith': {
        'Gender': 'Female',
        'Department': 'Neurology',
        'Diagnosis': 'Diabetes',
        'Admissions': '2025-02-20 09:15',
        'Medication': 'Metformin',
        'Clinical Insights': 'HbA1c levels improving.',
        'Discharge Summary': 'Diet and exercise regimen advised.'
    },
    'Alice': {
        'Gender': 'Female',
        'Department': 'Cardiology',
        'Diagnosis': 'Arrhythmia',
        'Admissions': '2025-02-05 16:45',
        'Medication': 'Amiodarone',
        'Clinical Insights': 'Requires ECG monitoring.',
        'Discharge Summary': 'Follow-up in 3 weeks.'
    },
    'Bob': {
        'Gender': 'Male',
        'Department': 'Cardiology',
        'Diagnosis': 'Heart Failure',
        'Admissions': '2025-01-15 10:30',
        'Medication': 'Carvedilol',
        'Clinical Insights': 'Monitor fluid retention.',
        'Discharge Summary': 'Scheduled for further tests.'
    },
    'Charlie': {
        'Gender': 'Male',
        'Department': 'Cardiology',
        'Diagnosis': 'Hypertension',
        'Admissions': '2025-01-10 12:20',
        'Medication': 'Lisinopril',
        'Clinical Insights': 'Stable BP levels.',
        'Discharge Summary': 'Review in 4 weeks.'
    },
    'David': {
        'Gender': 'Male',
        'Department': 'Neurology',
        'Diagnosis': 'Stroke',
        'Admissions': '2024-12-15 08:50',
        'Medication': 'Aspirin',
        'Clinical Insights': 'Under rehabilitation therapy.',
        'Discharge Summary': 'Neurological check-up in 1 month.'
    },
    'Eva': {
        'Gender': 'Female',
        'Department': 'Neurology',
        'Diagnosis': 'Epilepsy',
        'Admissions': '2025-01-05 14:10',
        'Medication': 'Levetiracetam',
        'Clinical Insights': 'Seizure frequency reduced.',
        'Discharge Summary': 'Continue medication and track seizures.'
    },
    'Frank': {
        'Gender': 'Male',
        'Department': 'Neurology',
        'Diagnosis': 'Migraine',
        'Admissions': '2025-02-02 11:55',
        'Medication': 'Sumatriptan',
        'Clinical Insights': 'Triggers identified and avoided.',
        'Discharge Summary': 'Recommended lifestyle changes.'
    },
    'Grace': {
        'Gender': 'Female',
        'Department': 'Oncology',
        'Diagnosis': 'Lung Cancer',
        'Admissions': '2024-11-25 15:30',
        'Medication': 'Chemotherapy',
        'Clinical Insights': 'Tumor responding to treatment.',
        'Discharge Summary': 'Scheduled for next chemo cycle.'
    },
    'Hannah': {
        'Gender': 'Female',
        'Department': 'Oncology',
        'Diagnosis': 'Breast Cancer',
        'Admissions': '2024-10-30 09:40',
        'Medication': 'Tamoxifen',
        'Clinical Insights': 'Stable post-surgery.',
        'Discharge Summary': 'Hormone therapy prescribed.'
    },
    'Ian': {
        'Gender': 'Male',
        'Department': 'Oncology',
        'Diagnosis': 'Leukemia',
        'Admissions': '2024-09-20 17:10',
        'Medication': 'Imatinib',
        'Clinical Insights': 'Blood counts improving.',
        'Discharge Summary': 'Continue targeted therapy.'
    },
    'Jack': {
        'Gender': 'Male',
        'Department': 'Orthopedics',
        'Diagnosis': 'Fracture',
        'Admissions': '2025-03-01 13:25',
        'Medication': 'Painkillers & Calcium Supplements',
        'Clinical Insights': 'Bone healing progressing.',
        'Discharge Summary': 'Physiotherapy advised.'
    },
    'Karen': {
        'Gender': 'Female',
        'Department': 'Orthopedics',
        'Diagnosis': 'Arthritis',
        'Admissions': '2025-02-10 10:05',
        'Medication': 'NSAIDs',
        'Clinical Insights': 'Joint inflammation reduced.',
        'Discharge Summary': 'Regular mobility exercises prescribed.'
    },
    'Leo': {
        'Gender': 'Male',
        'Department': 'Orthopedics',
        'Diagnosis': 'Osteoporosis',
        'Admissions': '2025-01-20 08:30',
        'Medication': 'Bisphosphonates',
        'Clinical Insights': 'Bone density improved.',
        'Discharge Summary': 'Annual DEXA scan scheduled.'
    },
    'Mia': {
        'Gender': 'Female',
        'Department': 'Pediatrics',
        'Diagnosis': 'Asthma',
        'Admissions': '2025-03-05 12:50',
        'Medication': 'Inhaler (Albuterol)',
        'Clinical Insights': 'Better breathing control.',
        'Discharge Summary': 'Daily monitoring recommended.'
    },
    'Noah': {
        'Gender': 'Male',
        'Department': 'Pediatrics',
        'Diagnosis': 'Pneumonia',
        'Admissions': '2025-02-18 14:00',
        'Medication': 'Antibiotics',
        'Clinical Insights': 'Lung infection clearing.',
        'Discharge Summary': 'Prescribed breathing exercises.'
    },
    'Olivia': {
        'Gender': 'Female',
        'Department': 'Pediatrics',
        'Diagnosis': 'Gastroenteritis',
        'Admissions': '2025-02-25 10:45',
        'Medication': 'ORS & Probiotics',
        'Clinical Insights': 'Hydration levels restored.',
        'Discharge Summary': 'Diet modification advised.'
    }
}

departments = {
    'Cardiology': {'total_patients': 120, 'avg_readmission_rate': 5.2, 'patients': ['John Doe', 'Alice', 'Bob', 'Charlie']},
    'Neurology': {'total_patients': 85, 'avg_readmission_rate': 4.8, 'patients': ['Jane Smith', 'David', 'Eva', 'Frank']},
    'Oncology': {'total_patients': 95, 'avg_readmission_rate': 6.1, 'patients': ['Grace', 'Hannah', 'Ian']},
    'Orthopedics': {'total_patients': 110, 'avg_readmission_rate': 3.9, 'patients': ['Jack', 'Karen', 'Leo']},
    'Pediatrics': {'total_patients': 75, 'avg_readmission_rate': 2.5, 'patients': ['Mia', 'Noah', 'Olivia']}
}

# Extract patient names for the selectbox options
patient_names = list(patient_data.keys())

# Define default patient
default_patient = st.session_state.get('selected_patient', "")

# Layout
col1, col2 = st.columns([1, 3])

with col1:
    st.header("Patient Data")

    selected_patient = st.selectbox("Search by name", [""] + patient_names, index=patient_names.index(default_patient) + 1 if default_patient in patient_names else 0)

    if selected_patient != "" and selected_patient in patient_data:
        patient_info = patient_data[selected_patient]
        st.success(f"Patient '{selected_patient}' found.")
    else:
        st.info("Please select a patient.")
        if st.button("Create New Patient"):
            st.switch_page("pages/New_Patient.py")

with col2:
    if selected_patient != "":
        st.header(f"Patient Details: {selected_patient}")

        # Blocks for Diagnosis and Admissions
        diag_col, adm_col = st.columns(2)

        with diag_col:
            st.subheader("Diagnosis")
            st.write(patient_info['Diagnosis'])

        with adm_col:
            st.subheader("Admissions")
            st.write(patient_info['Admissions'])

        # Block for Patient Data and Chart with Tabs
        st.subheader("Patient Data and Chart")
        patient_tabs = st.tabs(["Medication", "Clinical Insights", "Discharge Summary"])

        with patient_tabs[0]:
            st.write(patient_info['Medication'])

        with patient_tabs[1]:
            st.write(patient_info['Clinical Insights'])

        with patient_tabs[2]:
            st.write(patient_info['Discharge Summary'])


        st.subheader("Readmission Risk Analysis")
        # Action buttons for patient data
        col1, col2,col3 = st.columns(3, gap="small")
        with col1:
            st.button("Assess Readmission Risk", key="readmission_risk_button", help="Assess the risk of readmission for this patient.")
        with col2:
            st.button("View Readmission History", key="readmission_history_button", help="View the readmission history for this patient.")
        with col3:
            st.button("Analyze Clinical Notes", key="analyze_notes_button", help="Analyze clinical notes using AI and LLMs.")
        # Export report button  
        st.subheader("Export Report")
        st.download_button(
    label="📥 Export Report",
    data="Patient report content here",  # Replace with actual data
    file_name="patient_report.txt",      # Replace with desired file name
    mime="text/plain",                   # Replace with appropriate MIME type
    key="export_report_button",
    help="Export the report for this patient."
)        
