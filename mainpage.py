# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:27:00 2023

@author: Edre MA
"""

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

#logo set

col1, col2, col3 = st.columns(3)

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image("smartlogo.png",width=150)
    
#fixing width of columns
    
st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)
    
#header

from streamlit_extras.colored_header import colored_header

colored_header(
    label="ID INVESTIGATOR :flag-my:",
    description="Malaysian infectious disease investigator",
    color_name="violet-70"
)

#login
import time

password = st.text_input("Keyword", value="", type="password")
if password=="idimy23":
    st.success("Welcome!")
    st.balloons()
    time.sleep(3)
    switch_page("instruction")
        