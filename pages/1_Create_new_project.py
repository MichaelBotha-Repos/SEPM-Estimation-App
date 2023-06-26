import streamlit as st


st.title('Creeate a new project')


with st.form('new_pj'):
    task = st.text_input('Add new task')
    task_description = st.text_input('Add task description')
    task_estimation = st.text_input('Add task estimation')
    materials = st.text_input('Add materials')
    staff = st.text_input('Add staff')

    submitted = st.form_submit_button("Submit")