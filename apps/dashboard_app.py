# %%
from email import header
import streamlit as st
import pandas as pd
import numpy as np
import re

import streamlit.components.v1 as components

# add an import to Hydralit
from hydralit import HydraHeadApp

from apps.extras.speckle_data import *
from apps.extras.md_to_df import md2df
# from helpers.speckle_data import get_speckle_df

# %%


@st.cache
def load_data(stream_id):
    df = get_speckle_df(stream_id=stream_id)
    return df


def speckle_iframe(df, stream_id,  iframe_h=500):
    urls = []
    for index, row in df.iterrows():
        url = f"https://speckle.xyz/embed?stream={stream_id}&branch={row.branch}"
        components.iframe(url, height=iframe_h)
        urls.append(url)
    return urls


# %%
# create a wrapper class
class DashBoardApp(HydraHeadApp):

    def __init__(self, title='Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

# wrap all your code in this method and you should be done
    def run(self):

        ######################################
        # PROJECT INFO

        PROJECT_NAME = 'TEST NAME'
        PROJECT_ID = "23/00000"
        LOCATION = 'London, UK'
        CLIENT = 'Hoare Lea'
        LAST_UPDATE = '21/01/2022'
        CONSULTANT = 'Pablo Arango'

        project_details = {
            'Project': PROJECT_NAME,
            "Project ID": PROJECT_ID,
            "Location": LOCATION,
            "Client": CLIENT,
            "Last Update": LAST_UPDATE,
            "Consultant": CONSULTANT
        }

        ############ HEADER ##################

        # company logo on top
        st.sidebar.image(
            "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

        # set 2 columns
        col1, col2 = st.columns([2, 1])

        col1.markdown(f""" 
        # {PROJECT_NAME}
        ***{CONSULTANT} | Hoare Lea LLP.***

        Sample description of the project with replacemen variables such as **{LOCATION}** **{CLIENT}** **{LAST_UPDATE}** and any other variable
        
        list of analyses present number of revisions
        """)
        st.write('---')

        # Create Data frame with project properties
        project_details_df = pd.DataFrame(list(project_details.items()),
                                          columns=['Property', 'Value'])
        project_details_df.set_index('Property', inplace=True)

        # # Inject CSS with Markdown
        # st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # insert table second column
        col2.write(project_details_df)

        ######################################
        # SIDEBAR
        st.sidebar.header('Set Speckle Stream ID')
        STREAM_ID = st.sidebar.text_input('Speckle ID', '0b7b9e7705')

        # Sidebar - Revision Selection
        speckle_df = load_data(stream_id=STREAM_ID)
        speckle_df = speckle_df[speckle_df.revision != 'globals'] # remove global
<<<<<<< HEAD
=======

>>>>>>> c12ed8ab495cf54464f5ad2003091e528abb55f5
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

        # ######################################
        # # MAIN CONTENT

        # read markdown dataframe
        df_md = pd.read_excel('apps/data/df_markdown.xlsx', dtype="string")

        # st.title(sel_topic.upper())

        # debug
        # with st.expander('Dataframe'):
        #     st.write(df_md)

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

        # set 2 columns
        col3, col4 = st.columns([1, 1])

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

        # with col4:
        urls = speckle_iframe(df_sel_metric, stream_id=STREAM_ID)
        
        #################################################################
        # MANUAL REMARKS
        # makes sense to send the remarks in an Excel file with the topic coordinates 
        # then the issue is how to upload the results? 
        
        
# %%
