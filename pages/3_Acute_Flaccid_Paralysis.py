# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:11:18 2023

@author: Edre MA
"""

#library

import streamlit as st
from streamlit_extras.mention import mention
from markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page

#header setting

col1, col2, col3 = st.columns(3)

with col1:
    st.title(":heavy_exclamation_mark: ACUTE FLACCID PARALYSIS")
    
with col2:
    st.image("27011.jpg")

st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

#content
st.subheader("[1] Organism/causes")
x=st.selectbox("Differential diagnosis",('Poliovirus','GBS','central nervous system (CNS) infection', 'CNS tumors', 'transverse myelitis', 'myasthenia gravis', 'hypokalemic paralysis','botulism'), index=7)
if x=="Poliovirus":
    switch_page("Acute_Poliomyelitis")
st.write("")
st.subheader("[2] Incubation period")
st.write("Depends on diagnosis")
st.write("")
st.subheader("[3] Period of communicability")
st.write("Depends on diagnosis")
st.write("")
st.subheader("[4] Case Definition")
st.write("")
st.write(":mag: Clinical case definition")
st.write("Any child age less than 15 years developed an acute onset of flaccid paralysis should\
         have poliovirus infection ruled out.")
st.write("")  
st.write(":mag: Case classification")  
st.write("a. Discard 1: AFP case with adequate stool and on follow-up after 60 days of onset,\
has no residual paralysis.")  
st.write("b. Discard 2: AFP case with inadequate stool and on follow-up after 60 days of onset,\
has no residual paralysis")   
st.write("c. Discard 3: AFP case with inadequate stool with residual paralysis on 60 days\
follow-up OR loss to follow-up OR died before 60 days follow-up. Classification done\
by the Expert Group Review.")  
st.write("")
st.header("[5] Prevention & Control")
st.write("")
st.write(":one: Primary")
mdlit("""[violet] Health promotion : [/violet]Educate on warning sign such as sudden inability to walk""")
mdlit("""[orange] Specific protection : [/orange]Vaccination such as OPV as per NIP: \
      @(https://immunise4life.my/wp-content/uploads/2021/04/2-NIP-Schedule-1024x638.jpg)""")
st.write(":two: Secondary")
mdlit("""[green] Early detection : [/green]Two stool specimens should be collected with interval between the first and second stool\
      at least 24 hours apart; and both samples are taken within 14 days of onset of\
      paralysis. It is classified as adequate stool.""") 
mdlit("""[violet] Prompt treatment : [/violet]Non-specific""")
st.write(":three: Tertiary") 
mdlit("""[red] Disability limitation : [/red]ICU management if airway compromised""")
mdlit("""[blue] Rehabilitation : [/blue]OT and PT""")        