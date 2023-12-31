import streamlit as st
import logging
import os

# We are going to create a directory and configure our logger to save the logs to the file in that directory
try:
    # Location of directory
    logs_directory = "logs/"

    # Create logs directory if it doesn't exist
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    # Configure logging
    logging.basicConfig(filename=logs_directory + 'app.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

except OSError as e:
    print("Error creating directory or setting up logging:", str(e))

st.title('Select a function from the sidebar :four_leaf_clover:')
st.divider()
st.header('Instructions :book:')
st.subheader('Create a new project: :sparkles:')
st.text('Select the create a new project section on the sidebar.')
st.text('Assign a name to the project and submit, you should see a success message.')
st.caption('NOTE: the created project will be empty and you will need to add tasks, materials and staff records.')
st.divider()
st.subheader('Edit project: :wrench:')
st.text('To add records select the edit section from the sidebar.')
st.text('Choose the project you want to edit.')
st.text('When the project is chosen three tabs will appear: tasks, materials and staff.')
st.text('Use the "Add new" section to add a record.')
st.text('Then use the editable table to modify the records added.')
st.caption('NOTE: for the allocated staff staff section in tasks use the assigned resource corresponding staff ID')
st.divider()
st.subheader('Total costs: :dollar:')
st.text('To see total costs select the costs section on the sidebar and choose a project.')
st.text('Costs will automatically be displayed and summarized.')

st.sidebar.info('Cost calculator app')

logging.warning('App started - if this message is not shown: issue with streamlit library')
