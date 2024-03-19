import streamlit as st
import langchain_helper

st.title("Supplier Main Products and Leed Times by Country")

country = st.sidebar.selectbox("Pick a Country", ("United States", "China", "Mexico", "South East Asia", "Eastern Europe", "Middle East and Africa", "India"))

if country:
    response = langchain_helper.generate_supplier_name_and_items(country)
    st.header(response['supplier_name'].strip())
    product_items = response['product_items'].strip().split(",")
    st.write("**Main Products and Parts**")
    for item in product_items:
        st.write("-", item)

