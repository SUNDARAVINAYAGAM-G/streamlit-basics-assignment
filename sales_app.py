# sales_app.py

import streamlit as st
import pandas as pd

# Title and Subheader
st.title("Sales Summary Dashboard")
st.subheader("Interactive app to view and filter product sales by category")

# Create hardcoded dataset
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Office"],
    "Sales": [50000, 8000, 12000, 30000, 15000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")

# Get unique categories
categories = df["Category"].unique()

# Selectbox in sidebar
selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Filter DataFrame
filtered_df = df[df["Category"] == selected_category]

# Display filtered table
st.write(f"Showing sales for category: {selected_category}")
st.dataframe(filtered_df)

# Line chart of Sales
st.line_chart(filtered_df["Sales"])