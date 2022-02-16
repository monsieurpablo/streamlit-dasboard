#when we import hydralit, we automatically get all of Streamlit
from hydralit import HydraApp
import hydralit_components as hc
import streamlit as st
import apps

#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Hoarelea Web Toolkit', page_icon="🧰",layout='wide',initial_sidebar_state='auto',)

if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    over_theme = {'txc_inactive': '#FFFFFF',
                #   'txc_active': '#31333F',
                #   'option_active': '#F0F2F6',
                  'menu_background': '#31333F'
                  }
    
    app = HydraApp(title='Hoare Lea Web Toolbox',favicon="", 
                   hide_streamlit_markers = True,
                   use_navbar = True, 
                   navbar_sticky = True, 
                   navbar_animation= False,
                   layout='wide', # centered or wide
                   navbar_theme = over_theme,
                   allow_url_nav = True
                   )
  
    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
    app.add_app("Roadmap", icon="⚒️", app=apps.RoadmapApp(title='Roadmap'))
    app.add_app("Interactive Dashboard", icon="💻", app=apps.DashBoardApp(title='Dashboard'))
    
    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    #app.add_loader_app(apps.MyLoadingApp(delay=5))
    # app.add_loader_app(apps.QuickLoaderApp())
    
    #run the whole lot
    app.run()