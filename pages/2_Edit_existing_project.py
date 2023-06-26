import streamlit as st

st.title('Edit existing project')
st.divider()

option = st.selectbox(
    'Available projects:',
    ('Project 1', 'Project 2', 'Project 3'))

st.write('You selected:', option)