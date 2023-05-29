# -*- coding: utf-8 -*-
"""
Created on Tue May 30 00:14:00 2023

@author: Edre MA
"""

import streamlit as st
from markdownlit import mdlit

st.write("HOW TO USE THIS APP")
st.write("")
st.write("1. Choose the disease or condition of interest from the app sidebar >")
st.write("2. A :heavy_exclamation_mark: signifies urgent notification and action within 24 hours")
st.write("3. A :large_yellow_circle: signifies notification within 7 days")
st.write("4. Contains 5 important points, which are organism, incubation period,\
         communicable period or mode of transmission, case definition and prevention/control\
         measures")
st.write("5. Feel free to use any clickable links and interactive widgets to get more info")
st.write("")
mdlit("""Note: To check the ICD-10 coding, click here: @(https://icd10cmtool.cdc.gov/?fy=FY2023)""")
         