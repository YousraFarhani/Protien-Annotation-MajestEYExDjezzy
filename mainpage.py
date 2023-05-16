import streamlit as st
from streamlit import session_state

st.markdown(" ")
st.sidebar.markdown("# Welcome screen")



image = st.image('img.png', width=1300)

left_column, centered_column, col, right_column = st.columns(4)
# You can use a column just like st.sidebar:
col.button('LET''S GET STARTED !  ')
