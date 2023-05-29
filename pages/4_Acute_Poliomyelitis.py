# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:11:18 2023

@author: Edre MA
"""

#library

import streamlit as st
from streamlit_extras.mention import mention
from markdownlit import mdlit

#header setting

col1, col2, col3 = st.columns(3)

with col1:
    st.title(":heavy_exclamation_mark: ACUTE POLIOMYELITIS")
    
with col3:
    st.image("Polio-3-chains.png", width=150)

st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

#content
st.header("ICD-10 : A80")
st.subheader("[1] Organism/causes")
st.write("Poliovirus")
st.write("")
st.subheader("[2] Incubation period")
st.write("Non-paralytic: 3-6 days. Paralysis: 7-21 days ")
st.write("")
st.subheader("[3] Transmission")
st.write("Fecal-oral or oral-oral")
st.write("")
st.subheader("[4] Case Definition")
st.write("")
st.write(":mag: Clinical case definition")
st.write("A disease due to poliovirus infection, often characterised by an acute onset of flaccid\
paralysis.")
st.write("")  
st.write(":mag: Criteria for diagnosis")  
st.write("a. poliovirus is isolated (either wild type or vaccine strain) OR")  
st.write("b. positive serology (4 fold or greater rise in Ab) OR")   
st.write("c. epidemiological linkage to confirmed case.")  
st.write("")
st.subheader("[5] Prevention & Control")
st.write("")
st.write(":one: Primary")
mdlit("""[violet] Health promotion : [/violet]Educate on warning sign such as sudden inability to walk""")
mdlit("""[orange] Specific protection : [/orange]OPV at 2,3,5 months as per NIP: \
      @(https://immunise4life.my/wp-content/uploads/2021/04/2-NIP-Schedule-1024x638.jpg)""")
st.write(":two: Secondary")
mdlit("""[green] Early detection : [/green]Two stool specimens should be collected with interval between the first and second stool\
      at least 24 hours apart; and both samples are taken within 14 days of onset of\
      paralysis. It is classified as adequate stool.""") 
mdlit("""[violet] Prompt treatment : [/violet]Non-specific""")
st.write(":three: Tertiary") 
mdlit("""[red] Disability limitation : [/red]ICU management if airway compromised""")
mdlit("""[blue] Rehabilitation : [/blue]OT and PT""")        
        
