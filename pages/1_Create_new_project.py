from time import sleep
import streamlit as st
from project import ProjectFromGui
import sqlite3
import logging

db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()
st.header('Create a new project :pushpin:')

with st.form('new_pj', clear_on_submit=True):
    name_pj = st.text_input('Insert name')

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name_pj != "":
            ProjectFromGui.new_project(db_connection_cursor, name_pj)
            st.success('Success!')
            st.balloons()
            sleep(2)
            st.experimental_rerun()
        else:
            st.warning("Please enter a name first")
try:
    projects_list = ProjectFromGui.get_projects(db_connection_cursor)
except:
    logging.warning('Project table not created')
    st.warning('No projects yet, the script has stopped')
    st.stop()

st.header('Delete project :x:')

with st.form('input'):
    if len(projects_list) > 0:
        option = st.selectbox(
            'Available projects:',
            projects_list)
    else:
        logging.warning('empty project list')
        st.warning('No projects, create a project first')

    submit = st.form_submit_button('Delete project')

    if submit:
        # We prevent processing the delete command if there is nothing to delete
        if len(projects_list) > 0:
            ProjectFromGui.delete_project(db_connection_cursor, option)
            st.experimental_rerun()
        else:
            st.warning("There is nothing to delete here")

st.sidebar.info('Cost calculator app')
