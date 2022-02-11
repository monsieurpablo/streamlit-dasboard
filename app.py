#when we import hydralit, we automatically get all of Streamlit
from hydralit import HydraApp
import streamlit as st
import apps

#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Hoarelea Web Toolkit', page_icon="🧰",layout='wide',initial_sidebar_state='expanded',)

if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    
    app = HydraApp(title='Hoare Lea Web Toolbox',favicon="🧰")
  
    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
    app.add_app("Interactive Dashboard", icon="💻", app=apps.DashBoardApp(title='Dashboard'))
    #run the whole lot
    app.run()