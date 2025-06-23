import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stylable_container import stylable_container

# Set page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Home Button
if st.button("⌂ Home"):
    st.switch_page("Home.py")

st.title("🏥 Hospital Overview")
st.text("Comprehensive insights into hospital performance")

# ---------------- DATA ----------------
# Patient Data
patient_data = {
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

# Department Data
departments = {
    'Cardiology': {'total_patients': 120, 'avg_readmission_rate': 5.2},
    'Neurology': {'total_patients': 85, 'avg_readmission_rate': 4.8},
    'Oncology': {'total_patients': 95, 'avg_readmission_rate': 6.1},
    'Orthopedics': {'total_patients': 110, 'avg_readmission_rate': 3.9},
    'Pediatrics': {'total_patients': 75, 'avg_readmission_rate': 2.5}
}

# ---------------- METRICS SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    # Total Patients and Readmission Rate
    total_no_patients = sum(dept["total_patients"] for dept in departments.values())
    st.metric(label="🏥 Total Patients", value=total_no_patients)
with col2:
    total_readmission_rate = np.mean([dept['avg_readmission_rate'] for dept in departments.values()])
    st.metric(label="📈 Average Readmission Rate (%)", value=f"{total_readmission_rate:.2f}%")


# ---------------- DEPARTMENT-WISE READMISSION METRICS ----------------
st.markdown("### 📉 Department-wise Readmission Rates")
# Department Dropdown
col3,col = st.columns([1,4])
with col3:
    department = st.selectbox("📊 Select Department", list(departments.keys()))
    selected_dept_data = departments[department]
    # Show Department Metrics
with col:
    st.text("")

col4, col5 = st.columns(2)

with col4:
    st.metric(label="🏥 Total Patients", value=selected_dept_data['total_patients'])

with col5:
    st.metric(label="📈 Readmission Rate (%)", value=f"{selected_dept_data['avg_readmission_rate']}%")

# Improve metric styling
style_metric_cards(border_left_color="#1f77b4", border_radius_px=10, box_shadow=True)

# ---------------- GENDER RATIO PIE CHART ----------------
st.markdown("### 📊 Gender Ratio of Patients")

col6, col7, col8, col9= st.columns(4)

gender_counts = {"Male": 0, "Female": 0}
for patient in patient_data.values():
    gender_counts[patient["Gender"]] += 1

# Pie Chart
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(
    gender_counts.values(),
    labels=gender_counts.keys(),
    autopct='%1.1f%%',
    startangle=90,
    colors=["#3498db", "#e74c3c"]
)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

common_css_styles = """
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ccc;
    background-color: white;
    """

with stylable_container(
    key="gender_chart",
    css_styles=common_css_styles,
):
    with col6:
        st.pyplot(fig)
    with col7:
        st.text("")
    with col8:
        st.text("")
    with col9:
        st.text("")



# ---------------- OCCUPANCY RATE GRAPH ----------------
st.markdown("### 🏥 Hourly Occupancy Rate")

# Convert Admissions into Hourly Data
admission_hours = [int(pd.to_datetime(patient['Admissions']).hour) for patient in patient_data.values()]
hourly_occupancy = pd.Series(admission_hours).value_counts().sort_index()

# Hour Slider
hour_slider = st.slider("📌 Select Hour", min_value=0, max_value=23, value=12, step=1)
occupancy_filtered = hourly_occupancy.get(hour_slider, 0)

# Display Selected Hour Occupancy
st.info(f"📌 Number of Admissions at {hour_slider}:00, {occupancy_filtered}")
col, col2= st.columns(2)
with col:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(hourly_occupancy.index, hourly_occupancy.values, color="#27ae60")
    ax.axvline(hour_slider, color="red", linestyle="--", label="Selected Hour")
    ax.set_xticks(range(0, 24, 1))
    ax.set_xlabel("Hour of the Day")
    ax.set_ylabel("Number of Admissions")
    ax.legend()
    ax.set_title("Hourly Occupancy Rate")
    ax.set_facecolor("#f0f0f0")  # Set background color for better visibility
    # Add background container for better visibility
    with stylable_container(
        key="occupancy_chart",
        css_styles=common_css_styles,
    ):
        st.pyplot(fig)
with col2:
    # Simulate 7-day admissions
    days = pd.date_range(end=pd.Timestamp.today(), periods=7)
    admissions = np.random.randint(50, 130, size=7)
    df = pd.DataFrame({"Date": days, "Admissions": admissions})

    fig = px.line(df, x="Date", y="Admissions", title="🕒 Weekly Admissions Trend")
    st.plotly_chart(fig, use_container_width=True)


# ---------------- PATIENT LIST ----------------
st.markdown("### 📋 Patient List")

# Patient List Table
patient_df = pd.DataFrame.from_dict(patient_data, orient='index')
patient_df.reset_index(inplace=True)
patient_df.rename(columns={'index': 'Patient Name'}, inplace=True)
patient_df['Admissions'] = pd.to_datetime(patient_df['Admissions']).dt.strftime('%Y-%m-%d %H:%M')

# Display Patient List
st.dataframe(patient_df, use_container_width=True)
# ---------------- FOOTER ----------------
st.markdown("---")
st.button("📞 Contact Us")
st.button("📧 Feedback")