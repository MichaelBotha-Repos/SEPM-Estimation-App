import sqlite3
import streamlit as st
from project import Project_from_gui as pj
from task import Task
from material import Materials

db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()

projects_list = pj.get_projects(db_connection_cursor)


st.title('Edit existing project')
st.divider()

if len(projects_list) > 0:
    option = st.selectbox(
        'Available projects:',
        projects_list)
else:
    st.warning('No projects, create a project first')

st.write('You selected:', option)

st.divider()

st.subheader('Task list:')
if option:
    tasks_list = pj.get_tasks(db_connection_cursor, option)
    if len(tasks_list) >= 1:
        
        edited_df = st.data_editor(tasks_list, hide_index=True, disabled=['task_id'])
        st.button('Send update tasks', on_click=Task.update_tasks(db_connection, edited_df, option))
    else:
        st.warning('There are no tasks yet')

    st.divider()

    st.subheader('Add task')
    with st.form('task_form', clear_on_submit=True):
        task_desc = st.text_input('Task description')
        task_est_1 = st.number_input('Estimation 1', value=0, step=1)
        task_est_2 = st.number_input('Estimation 2', value=0, step=1)
        task_est_3 = st.number_input('Estimation 3', value=0, step=1)
        task_est_chosen = st.number_input('Chosen estimation', value=0, step=1)
        task_staff = st.number_input('Allocated staff', value=0, step=1)
        
        submitted = st.form_submit_button('Submit')

        # formatting for sql query
        task_1 = int(task_est_1)
        task_2 = int(task_est_2)
        task_3 = int(task_est_3)
        task_chosen = int(task_est_chosen)
        task_staff = int(task_staff)

        if submitted:
            Task.add_task(db_connection_cursor, option, task_desc, task_1, task_2, task_3, task_chosen, task_staff)
            st.experimental_rerun()
st.divider()
st.subheader('Materials:')
if option:
    materials_list = pj.get_materials(db_connection_cursor, option)
    if len(materials_list) > 0:
        edited_df_m = st.data_editor(materials_list, hide_index=True, disabled=['material_id'])
        st.button('Send update materials', on_click=Materials.update_materials(db_connection, edited_df_m, option))
    else:
        st.warning('There are no materials yet')

    st.subheader('Add material')
    with st.form('material_form', clear_on_submit=True):
        material_desc = st.text_input('Material description')
        number_req = st.number_input('Number required', value=0, step=1)
        unit_cost = st.number_input('Unit cost', value=0, step=1)

        submitted = st.form_submit_button('Submit')

        # formatting for sql query
        number_req = int(number_req)
        unit_cost = int(unit_cost)

        if submitted:
            Materials.add_material(db_connection_cursor, option, material_desc, number_req, unit_cost)