from time import sleep
import streamlit as st
from project import Project_from_gui
import sqlite3


db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()
st.header('Create a new project')


with st.form('new_pj', clear_on_submit=True):
    name_pj = st.text_input('Insert name')

    submitted = st.form_submit_button("Submit")

    if submitted:
        Project_from_gui.new_project(db_connection_cursor, name_pj)
        st.success('Success!')
        st.balloons()
        sleep(2)
        st.experimental_rerun()
try:
    projects_list = Project_from_gui.get_projects(db_connection_cursor)
except:
    st.warning('No projects yet, the script has stopped')


st.header('Delete project')

with st.form('input'):
    if len(projects_list) > 0:
        option = st.selectbox(
            'Available projects:',
            projects_list)
    else:
        st.warning('No projects, create a project first')
        
    
    submit = st.form_submit_button('Delete project')

    if submit:
        Project_from_gui.delete_project(db_connection_cursor, option)

st.sidebar.info('Cost calculator app')