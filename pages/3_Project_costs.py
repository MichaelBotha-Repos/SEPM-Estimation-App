import streamlit as st
import sqlite3
from project import Project_from_gui as pj

db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()

try:
    projects = pj.get_projects(db_connection_cursor)
except:
    st.warning('No projects yet, the script has stopped')
    st.stop()


st.title('Project costs')
st.divider()

if len(projects) > 0:
    option = st.selectbox(
        'Available projects:',
        projects)
else:
    st.warning('No projects, create a project first')

if option:

    st.write('You selected:', option)

    st.divider()

    st.subheader('Total task and staff cost:')
    task_df = pj.get_tasks(db_connection_cursor, option)
    staff_df = pj.get_staff(db_connection_cursor, option)

    st.divider()

    st.subheader('Total materials cost:')
    material_df = pj.get_materials(db_connection_cursor, option)
    material_df['total'] = material_df['number_required'] * material_df['unit_cost']
    st.write(material_df)

    total = material_df['total'].sum()
    st.write('Total project\'s materials cost:', total)




