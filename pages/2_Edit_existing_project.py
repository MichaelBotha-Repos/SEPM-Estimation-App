import sqlite3
import streamlit as st
from project import Project_from_gui as pj
from staff import Staff
from task import Task
from material import Materials
import logging

db_connection = sqlite3.connect('estimations.db')
db_connection_cursor = db_connection.cursor()

try:
    projects_list = pj.get_projects(db_connection_cursor)
except:
    logging.warning('No projects - empty table or table not created')
    st.warning('No projects yet, the script has stopped')
    st.stop()


st.header('Edit existing project :wrench:')
st.divider()

if len(projects_list) > 0:
    option = st.selectbox(
        'Available projects:',
        projects_list)
else:
    logging.warning('no project, general edit')
    st.warning('No projects, create a project first')
    st.stop()

st.write('You selected:', option)

tab1, tab2, tab3 = st.tabs(["Task", "Material", "Staff"])


with tab1:
    st.subheader('Task list:')
    if option:
        st.text('When allocating staff please use staff ID')
        tasks_list = pj.get_tasks(db_connection_cursor, option)
        if len(tasks_list) >= 1:
            
            with st.form('task_form_1'):
                edited_df = st.data_editor(tasks_list, hide_index=True, disabled=['task_id'])

                submit_task = st.form_submit_button('Send update tasks')
                if submit_task:
                    Task.update_tasks(db_connection, edited_df, option)
        else:
            logging.warning('task table empty or not created')
            st.warning('There are no tasks yet')

        st.divider()

        st.subheader('Add task')
        with st.form('task_form_2', clear_on_submit=True):
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
        st.subheader('Delete task')
        with st.form('delete_task'):
            task_id_to_delete = st.number_input('Insert task id to delete', value=0, step=1)

            submit_del = st.form_submit_button('Delete task')
            if submit_del:
                Task.delete_task(db_connection_cursor, option, task_id_to_delete)
                st.experimental_rerun()


with tab2:
    st.subheader('Materials:')
    if option:
        materials_list = pj.get_materials(db_connection_cursor, option)
        if len(materials_list) > 0:

            with st.form('material_form_1'):
                edited_df_m = st.data_editor(materials_list, hide_index=True, disabled=['material_id'])
                mat_submit = st.form_submit_button('Send update materials')
                if mat_submit:
                    Materials.update_materials(db_connection, edited_df_m, option)
        else:
            logging.warning('material table empty or not created')
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
                st.experimental_rerun()

        with st.form('delete_material'):
            material_id_to_delete = st.number_input('Insert material id to delete', value=0, step=1)

            submit_del_m = st.form_submit_button('Delete material')
            if submit_del_m:
                Materials.delete_material(db_connection_cursor, option, material_id_to_delete)
                st.experimental_rerun()
            


with tab3:
    st.subheader('Staff:')
    if option:
        Staff_list = pj.get_staff(db_connection_cursor, option)
        if len(Staff_list) > 0:

            with st.form('staff_form_1'):
                edited_df_s = st.data_editor(Staff_list, hide_index=True, disabled=['Staff_id'])
                submit_staff = st.form_submit_button('Send update Staff')
                if submit_staff:
                    Staff.update_staff(db_connection, edited_df_s, option)
        else:
            logging.warning('staff table empty or not created')
            st.warning('There is no Staff yet')

        st.subheader('Add Staff')
        with st.form('Staff_form', clear_on_submit=True):
            Staff_desc = st.text_input('Staff designation')
            rate = st.number_input('Rate', value=0, step=1)

            submitted = st.form_submit_button('Submit')

            # formatting for sql query
            rate = int(rate)

            if submitted:
                Staff.add_staff(db_connection_cursor, option, Staff_desc, rate)
                st.experimental_rerun()

        with st.form('delete_staff'):
            staff_id_to_delete = st.number_input('Insert staff id to delete', value=0, step=1)

            submit_del_s = st.form_submit_button('Delete staff')
            if submit_del_s:
                Staff.delete_staff(db_connection_cursor, option, staff_id_to_delete)
                st.experimental_rerun()

st.sidebar.info('Cost calculator app')