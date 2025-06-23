import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import importlib.util

# Set page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
if st.button("⌂ Home"):
        st.switch_page("Home.py")
        
# Sample patient data
patient_data = {  # Using your provided dataset
    'John Doe': {'Gender': 'Male', 'Department': 'Cardiology', 'Admissions': '2025-03-10 14:30'},
    'Jane Smith': {'Gender': 'Female', 'Department': 'Neurology', 'Admissions': '2025-02-20 09:15'},
    'Alice': {'Gender': 'Female', 'Department': 'Cardiology', 'Admissions': '2025-02-05 16:45'},
    'Bob': {'Gender': 'Male', 'Department': 'Cardiology', 'Admissions': '2025-01-15 10:30'},
    'Charlie': {'Gender': 'Male', 'Department': 'Cardiology', 'Admissions': '2025-01-10 12:20'},
    'David': {'Gender': 'Male', 'Department': 'Neurology', 'Admissions': '2024-12-15 08:50'},
    'Eva': {'Gender': 'Female', 'Department': 'Neurology', 'Admissions': '2025-01-05 14:10'},
    'Frank': {'Gender': 'Male', 'Department': 'Neurology', 'Admissions': '2025-02-02 11:55'},
    'Grace': {'Gender': 'Female', 'Department': 'Oncology', 'Admissions': '2024-11-25 15:30'},
}

departments = {
    'Cardiology': {'total_patients': 120, 'avg_readmission_rate': 5.2},
    'Neurology': {'total_patients': 85, 'avg_readmission_rate': 4.8},
    'Oncology': {'total_patients': 95, 'avg_readmission_rate': 6.1},
    'Orthopedics': {'total_patients': 110, 'avg_readmission_rate': 3.9},
    'Pediatrics': {'total_patients': 75, 'avg_readmission_rate': 2.5}
}


# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center;'>🏥 Hospital Overview</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- METRICS SECTION ----------------
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    total_patients = len(patient_data)
    st.metric(label="👥 Total Patients", value=total_patients)

with col2:
    total_readmission_rate = np.mean([dept['avg_readmission_rate'] for dept in departments.values()])
    st.metric(label="📈 Total Readmission Rate", value=f"{round(total_readmission_rate, 2)}%")

with col3:
    selected_department = st.selectbox("📊 Select Department", list(departments.keys()), index=0)

# ---------------- GENDER RATIO PIE CHART ----------------
st.markdown("### 📊 Gender Ratio of Patients")

gender_counts = {"Male": 0, "Female": 0}
for patient in patient_data.values():
    gender_counts[patient["Gender"]] += 1

fig, ax = plt.subplots(figsize=(5, 3))
ax.pie(
    gender_counts.values(),
    labels=gender_counts.keys(),
    autopct='%1.1f%%',
    startangle=90,
    colors=["#3498db", "#e74c3c"]
)
ax.axis('equal')
st.pyplot(fig)

# ---------------- DEPARTMENT-WISE READMISSION METRICS ----------------
st.markdown("### 📉 Department-wise Readmission Rates")
dept_cols = st.columns(len(departments))

for idx, (dept, data) in enumerate(departments.items()):
    with dept_cols[idx]:
        st.metric(label=f"🏥 {dept}", value=f"{data['avg_readmission_rate']}%")

# ---------------- OCCUPANCY RATE GRAPH ----------------
st.markdown("### 🏥 Hourly Occupancy Rate")

# Convert Admissions into Hourly Data
admission_hours = [int(pd.to_datetime(patient['Admissions']).hour) for patient in patient_data.values()]
hourly_occupancy = pd.Series(admission_hours).value_counts().sort_index()

# Hour Slider
hour_slider = st.slider("📌 Select Hour", min_value=0, max_value=23, value=12, step=1)
occupancy_filtered = hourly_occupancy.get(hour_slider, 0)
# Display Selected Hour Occupancy
st.info(f"📌 Number of Admissions at {hour_slider}:00 → {occupancy_filtered}")

fig, ax = plt.subplots(figsize=(10, 3))
ax.bar(hourly_occupancy.index, hourly_occupancy.values, color="#27ae60")
ax.axvline(hour_slider, color="red", linestyle="--", label="Selected Hour")
ax.set_xticks(range(0, 24, 1))
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Number of Admissions")
ax.legend()
st.pyplot(fig)



