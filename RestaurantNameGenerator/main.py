import streamlit as st
import langchain_helper

st.title("Supplier Main Products and Leed Times by Country")

cuisine = st.sidebar.selectbox("Pick a Country", ("United States", "China", "Mexico", "South East Asia", "Eastern Europe", "Middle East and Africa", "India"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

