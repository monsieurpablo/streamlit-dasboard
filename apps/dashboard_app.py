# %%
import streamlit as st
import pandas as pd
import numpy as np

import streamlit.components.v1 as components

#add an import to Hydralit
from hydralit import HydraHeadApp

from apps.extras.speckle_data import *
# from helpers.speckle_data import get_speckle_df

# %%

@st.cache
def load_data(stream_id):
    df = get_speckle_df(stream_id=stream_id)
    return df

def speckle_iframe(df, stream_id,  iframe_h = 500):
    urls = []
    for index, row in df.iterrows():
        url = f"https://speckle.xyz/embed?stream={stream_id}&branch={row.branch}"
        components.iframe(url, height=iframe_h)
        urls.append(url)
    return urls


# %%
#create a wrapper class
class DashBoardApp(HydraHeadApp):

    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

#wrap all your code in this method and you should be done
    def run(self):
        ######################################
        # PROJECT INFO

        PROJECT_NAME = 'TEST NAME'
        PROJECT_ID = "23/00000"
        LOCATION = 'London, UK'
        CLIENT = 'Hoare Lea'
        LAST_UPDATE = '21/01/2022'

        project_details = {
            'Project Name':PROJECT_NAME,
            "Project ID" : PROJECT_ID,
            "Location" : LOCATION,
            "Client" : CLIENT,
            "Last Update" : LAST_UPDATE,
        }

        ############ HEADER ##################

        # company logo on top
        st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

        # set 2 columns
        col1, col2 = st.columns([2,1])

        col1.markdown(""" 
        # {{Project Name}}
        ***{{Consultant Name}} | Hoare Lea LLP.***

        Sample description of the project with replacemen variables such as {{location}} {{client}} {{date}} {{last_update}} and any other variable
        
        {{list of analyses present}}
        {{# of revisions}}
        """)
        st.write('---')


        # Create Data frame with project properties
        project_details_df = pd.DataFrame(list(project_details.items()), columns=['Property', 'Value'])
        project_details_df.set_index('Property', inplace= True)

        # insert table second column
        col2.table(project_details_df.astype(str))

        ######################################
        # SIDEBAR
        st.sidebar.header('Set Speckle Stream ID')
        STREAM_ID = st.sidebar.text_input('Speckle ID', '0b7b9e7705')
        
        # Sidebar - Revision Selection
        speckle_df = load_data(stream_id=STREAM_ID)
        
        st.sidebar.subheader('Select Revision')
        sorted_unique_revision = sorted(speckle_df.revision.unique())
        sel_rev = st.sidebar.selectbox('Revision', sorted_unique_revision, index=0) #select first
        
        # Filtering data
        # df_sel_rev = speckle_df[(speckle_df.revision.isin(sel_rev))]
        df_sel_rev = speckle_df[speckle_df.revision == sel_rev]
        
        # # Sidebar - Analysis selection
        st.sidebar.subheader('Select Analysis Topic')
        sorted_unique_topics = sorted(df_sel_rev.topic.unique())
        sel_topic = st.sidebar.selectbox('Topic', sorted_unique_topics, index=0) #select first
        
        # ######################################
        # # MAIN CONTENT
        
        st.title(sel_topic.upper())
        # Filtering data
        # df_sel_rev = speckle_df[(speckle_df.revision.isin(sel_rev))] #filter based on list
        df_sel_topic = df_sel_rev[df_sel_rev.topic == sel_topic]
        
        # debug
        with st.expander('Dataframe'):
            st.write(df_sel_topic)
            
        # Analysis selection
        sorted_unique_metrics = sorted(df_sel_topic.metric.unique())
        sel_metric = st.selectbox('Metric', sorted_unique_metrics, index=0) #select first
        st.write("---")
        
        df_sel_metric = df_sel_topic[df_sel_topic.metric == sel_metric]
        
        st.subheader(sel_metric.upper())
        
        urls = speckle_iframe(df_sel_metric, stream_id=STREAM_ID)   

        # ############################################################
        # Additional
        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    footer:after{
                        content:'Copyright @2022: Hoarelea'
                    }
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

        # Hide hosted with Streamlit ->
        hide_footer_style = """
        <style>
        .reportview-container .main footer {visibility: hidden;}    
        """
        st.markdown(hide_footer_style, unsafe_allow_html=True)
# %%
