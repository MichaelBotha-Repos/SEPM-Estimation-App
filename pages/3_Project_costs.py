import streamlit as st
import sqlite3
from project import Project_from_gui as pj
import pandas as pd

db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()

try:
    projects = pj.get_projects(db_connection_cursor)
except:
    st.warning('No projects yet, the script has stopped')
    st.stop()


st.header('Project costs :dollar:')
st.divider()

if len(projects) > 0:
    option = st.selectbox(
        'Available projects:',
        projects)
else:
    st.warning('No projects, create a project first')
    st.stop()

if option:

    st.write('You selected:', option)

    st.divider()

    st.subheader('Total staff cost divided by task:')
    task_df = pj.get_tasks(db_connection_cursor, option)
    staff_df = pj.get_staff(db_connection_cursor, option)

    new_df = pd.DataFrame()

    new_df['tasks'] = task_df['task_description']
    new_df['chosen_estimate'] = task_df['chosen_estimate']
    new_df['allocated_staff'] = task_df['allocated_staff']
    df2 = pd.merge(new_df, staff_df, left_on='allocated_staff', right_on='staff_id')
    df2['total'] = df2['chosen_estimate'] * df2['rate']
    st.dataframe(df2, hide_index=True)
    tot = df2['total'].sum()
    st.write('The total task cost for this project is:', tot)
    


    st.divider()

    st.subheader('Total materials cost:')
    material_df = pj.get_materials(db_connection_cursor, option)
    material_df['total'] = material_df['number_required'] * material_df['unit_cost']
    st.dataframe(material_df, hide_index=True)

    total = material_df['total'].sum()
    st.write('Total project\'s materials cost:', total)

st.sidebar.info('Cost calculator app')


