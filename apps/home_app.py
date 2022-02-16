from pathlib import Path

import streamlit as st
import numpy as np
import pandas as pd

#add an import to Hydralit
from hydralit import HydraHeadApp

def read_markdown(markdown_file):
    return Path(markdown_file).read_text()

#create a wrapper class
class HomeApp(HydraHeadApp):
    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------
        # company logo on top
        st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

        # set 2 columns
        col1, col2 = st.columns([2,1])

        col1.markdown(""" 
        # Interactive Report  V0.2
        ***Pablo Arango***

        Sample dashboard for showcasing the the great potential of web reporting
        utilizing **Python**, **Speckle** and **Streamlit** for creating compeling
        web-based reports integrating 3D geometry as well as Building Physics results
        into a engaging interactive report.
        """)
        st.write('---')
        