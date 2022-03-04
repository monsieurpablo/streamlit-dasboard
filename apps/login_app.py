from typing import Dict
import streamlit as st
import os
import pandas as pd

import streamlit_authenticator as stauth
from secrets import token_urlsafe


os.environ["GSHEET_ID"] = "17oH61DLGHjllLqrNOX2Tx8oc69qyYCEHrlkMvnDL1Tg"
SHEET_ID = os.environ.get('GSHEET_ID')


# Read-only google sheets dataframe without APY requirements
def read_gsheets(sheet_id, sheet_name) -> pd.DataFrame:
    # df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv") # first sheet only
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}")
    return df

# @st.cache(ttl=1200)
def load_users():
    return read_gsheets(SHEET_ID, 'Users')

def LoginApp():
    
    
    # Initialize the session state variable
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None

    # company logo on top
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)
    
    # Front-End
    st.markdown("<h1 style='text-align: center;'>Hoare Lea Login</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center'> Test users 'guest' & 'guest' </div>", unsafe_allow_html=True)
    
    # LOAD DATA
    
    # read database
    df_users = load_users()
    
    names = df_users.names.to_list()
    usernames = df_users.usernames.to_list()
    passwords = df_users.passwords.to_list()
    
    # names = st.secrets["stauth"]["names"]
    # usernames = st.secrets["stauth"]["usernames"]
    # passwords = st.secrets["stauth"]["passwords"]
    
    hashed_passwords = stauth.hasher(passwords).generate()
    authenticator = stauth.authenticate(names, usernames, hashed_passwords,
                                    'hl-dashboard', token_urlsafe(16), cookie_expiry_days=30)
    
    # set 2 columns
    space1, col,space2  = st.columns([1,3,1]) 
    
    with col:
    # Create login form
        name, authentication_status = authenticator.login('Login', 'main')
        
        
        if authentication_status:
            st.write('Welcome *%s*' % name)
        elif not authentication_status: 
            st.error('Username/password is incorrect')
        elif authentication_status is None:
            st.warning('Please enter your username and password')
    
    return name, authentication_status