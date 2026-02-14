import streamlit as st

# Page config
st.set_page_config(
    page_title="Data Tool Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Profiling", "Validation", "Settings"])

# Header
st.title("📊 Data Quality Platform")

# Dashboard page
if page == "Dashboard":
    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Files Processed", "128", "+12")
    col2.metric("Rules Applied", "342", "+18")
    col3.metric("Errors Found", "27", "-3")

    st.divider()

    st.subheader("Recent Activity")
    st.dataframe({
        "File Name": ["sales.xlsx", "users.csv", "inventory.xlsx"],
        "Status": ["Completed", "Completed", "Failed"],
        "Errors": [2, 0, 5]
    })

# Profiling page
elif page == "Profiling":
    st.subheader("Data Profiling")

    uploaded_file = st.file_uploader("Upload a dataset", type=["csv", "xlsx"])

    if uploaded_file:
        st.success("File uploaded successfully")
        st.write("Profiling results will appear here...")

# Validation page
elif page == "Validation":
    st.subheader("Validation Rules")

    rule = st.text_input("Enter rule name")
    severity = st.selectbox("Severity", ["Low", "Medium", "High"])

    if st.button("Add Rule"):
        st.success(f"Rule '{rule}' added with {severity} severity")

# Settings page
elif page == "Settings":
    st.subheader("Settings")

    theme = st.selectbox("Theme", ["Light", "Dark"])
    notifications = st.checkbox("Enable notifications")

    st.write("Preferences saved automatically.")
