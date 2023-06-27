from time import sleep
import streamlit as st
from project import Project_from_gui
import sqlite3


db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()
st.title('Create a new project')


with st.form('new_pj', clear_on_submit=True):
    name_pj = st.text_input('Insert name')

    submitted = st.form_submit_button("Submit")

    if submitted:
        Project_from_gui.new_project(db_connection_cursor, name_pj)
        st.success('Success!')
        st.balloons()
        sleep(2)
        st.experimental_rerun()