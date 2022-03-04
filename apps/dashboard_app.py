# %%
import streamlit as st
import pandas as pd
import numpy as np
import re
import os

import streamlit.components.v1 as components

# add an import to Hydralit
from hydralit import HydraHeadApp

from apps.extras.speckle_data import *
from apps.extras.md_to_df import md2df
# from helpers.speckle_data import get_speckle_df

# %%
SHEET_ID = os.environ.get('GSHEET_ID')


# speckle iframe from url
def speckle_iframe(df, stream_id,  iframe_h=500):
    urls = []
    for index, row in df.iterrows():
        url = f"https://speckle.xyz/embed?stream={stream_id}&branch={row.branch}"
        components.iframe(url, height=iframe_h)
        urls.append(url)
    return urls

# Read-only google sheets dataframe without APY requirements
def read_gsheets(sheet_id, sheet_name) -> pd.DataFrame:
    # df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv") # first sheet only
    df = pd.read_csv(
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}")
    return df


def convert_to_fstring(string:str):
        fstring = f'f"""{string}"""'
        compiled_fstring = compile(fstring, '<fstring>', 'eval')
        return compiled_fstring

# Speckle data
@st.cache(ttl=600)
def load_data(stream_id):
    df = get_speckle_df(stream_id=stream_id)
    return df

# Descriptions dataframe
# @st.cache()
def load_descriptions() -> pd.DataFrame:
    return read_gsheets(SHEET_ID, 'Descriptions')

# Remarks dataframe
# @st.cache()
def load_remarks() -> pd.DataFrame:
    return read_gsheets(SHEET_ID, 'CustomRemarks')

# Remarks dataframe
# @st.cache()
def load_project_info() -> pd.DataFrame:
    return read_gsheets(SHEET_ID, 'ProjectInfo')



# %%
# create a wrapper class
def DashBoardApp():

    #############################################################################
    # SIDEBAR
    # company logo on top
    st.sidebar.image(
        "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)
    
    
    st.sidebar.header('Set Speckle Stream ID')
    STREAM_ID = st.sidebar.text_input('Speckle ID', '0b7b9e7705')

    # Sidebar - Revision Selection
    speckle_df = load_data(stream_id=STREAM_ID)
    speckle_df = speckle_df[speckle_df.revision != 'globals']  # remove global

    # st.write(speckle_df)

    st.sidebar.subheader('Select Revision')
    sorted_unique_revision = sorted(speckle_df.revision.unique())
    sel_rev = st.sidebar.selectbox(
        'Revision', sorted_unique_revision, index=0)  # select first

    # Filtering data
    # df_sel_rev = speckle_df[(speckle_df.revision.isin(sel_rev))] # use for list
    df_sel_rev = speckle_df[speckle_df.revision == sel_rev]

    # # Sidebar - Analysis selection
    st.sidebar.subheader('Select Analysis Topic')
    sorted_unique_topics = sorted(df_sel_rev.topic.unique())
    sel_topic = st.sidebar.selectbox(
        'Topic', sorted_unique_topics, index=0)  # select first

    #############################################################################
    # MAIN CONTENT

    # PROJECT INFO
    
    # load project data
    project_details = load_project_info()
    
    # filter data for the speckle stream ID
    sel_project = project_details[project_details.speckleID == STREAM_ID]
    
    # ############ HEADER ###############################################################################################

    # compose the header
    st.header(sel_project.projectName.iloc[0])

    # convert to fstring from raw text
    # https://stackoverflow.com/questions/47339121/how-do-i-convert-a-string-into-an-f-string
    # this can be done in two ways -> 1) directly with the DF df.text.iloc[0] but is complex to input in the database or 
    # 2) convert to dictionary and access it ['key']
    
    # convert dataframe to dict
    sel_project_dict = sel_project.to_dict('records')[0]
    
    body = sel_project_dict['text']
    body_exp = sel_project_dict['detailedText']
    
    def hello_world():
        return 'Hello World Fuction!'
    
    st.write(eval(convert_to_fstring(body)), unsafe_allow_html=True)
    with st.expander('More Info'):
        st.write(eval(convert_to_fstring(body_exp)), unsafe_allow_html=True)

    st.write('---')
    
    # debug
    # st.write(sel_project.T)

    #############################################################################
    # BODY
    
    # read markdown dataframe
    # df_md = pd.read_excel('apps/data/df_markdown.xlsx', dtype="string") # read local
    df_md =load_descriptions() # read gsheets 

    # debug
    # with st.expander('Dataframe'):
    #     st.write(df_md)

    # 
    df_md_sel_topic = df_md[df_md.speckleName == sel_topic]
    st.header(df_md_sel_topic.header.iloc[0])
    st.write(df_md_sel_topic.text.iloc[0])

    with st.expander('Technichal details'):
        st.write(df_md_sel_topic.detailedText.iloc[0])

    # Filtering data
    # df_sel_rev = speckle_df[(speckle_df.revision.isin(sel_rev))] #filter based on list
    df_sel_topic = df_sel_rev[df_sel_rev.topic == sel_topic]

    # # debug
    # with st.expander('Dataframe'):
    #     st.write(df_sel_topic)

    # Analysis selection
    sorted_unique_metrics = sorted(df_sel_topic.metric.unique())
    sel_metric = st.selectbox(
        'Metric', sorted_unique_metrics, index=0)  # select first
    st.write("---")

    df_sel_metric = df_sel_topic[df_sel_topic.metric == sel_metric]

    # with col3:
    if sel_metric in df_md.speckleName.values:

        df_md_sel_metric = df_md[df_md.speckleName == sel_metric]

        st.subheader(df_md_sel_metric.header.iloc[0])
        st.write(df_md_sel_metric.text.iloc[0])
        with st.expander('Technichal details'):
            st.write(df_md_sel_metric.detailedText.iloc[0])
    else:
        st.subheader(f"Analysis for {sel_metric.upper()}")
    # set 2 columns

    # with col3:
    urls = speckle_iframe(df_sel_metric, stream_id=STREAM_ID)

    #################################################################
    # CUSTOM REMARKS

    df_remarks =load_remarks() # read gsheets 
    
    # filter results
    df_remarks = df_remarks[(df_remarks.speckleID == STREAM_ID) & (df_remarks.rev == sel_rev)]
    
    # st.write(STREAM_ID)
    # st.write(STREAM_ID in df_remarks.speckleID.unique())
    
    # filter the comments for each variable if exist for this project
    
    if (sel_metric in df_remarks.speckleName.values):
    
        df_sel_remarks = df_remarks[df_remarks.speckleName == sel_metric]

        st.subheader('Remarks')
        st.write(df_sel_remarks.text.iloc[0])
        with st.expander('Technichal details'):
            st.write(df_sel_remarks.detailedText.iloc[0])
    else:
        pass
        # st.subheader(f"Analysis for {sel_metric.upper()}")
    
    # debug
    # st.write(df_remarks)
    # st.write(df_sel_remarks)


# %%
