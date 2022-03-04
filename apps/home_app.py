from pathlib import Path

import streamlit as st
import base64


# #add an import to Hydralit
# from hydralit import HydraHeadApp

def read_markdown(markdown_file):
    return Path(markdown_file).read_text()

#create a function class
def HomeApp():
    # company logo on top
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

    # set 2 columns
    space1, col,space2  = st.columns([1,3,1])
    with col:
        
        st.markdown("<h1 style='text-align: center;'>Interactive Report  V0.2</h1>", unsafe_allow_html=True)

        st.markdown(""" 
        Sample dashboard for showcasing the the great potential of web reporting
        utilizing **Python**, **Speckle** and **Streamlit** for creating compeling
        web-based reports integrating 3D geometry as well as Building Physics results
        into a engaging interactive report.
        """)
        st.write('---')
        
        # # from url
        # st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
        
        """### gif from local file"""
        file_ = open("apps/data/dashboard.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        # # add gif of the platform
        # st.markdown(
        #     f'<img src="data:image/gif;base64,{data_url}" alt="dashboard Pablo Arango" width="500" />',
        #     unsafe_allow_html=True,
        # )
    
        
        