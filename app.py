#when we import hydralit, we automatically get all of Streamlit
import streamlit as st
import hydralit_components as hc
import apps

# Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Hoarelea Web Toolkit', page_icon="🧰",layout='wide',initial_sidebar_state='auto')

# Session Initialization
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

# If logged in -> Show all the tabs
if st.session_state['authentication_status']:
    # if st.session_state["role"] == "admin":
    menu_data = [
            {'icon': "", 'label': "Roadmap"},
            {'icon': "", 'label': "Dashboard"},
            {'icon': "", 'label': "Login"},
        ]
elif st.session_state['authentication_status'] == None:
    menu_data = [
            {'icon': "", 'label': "Login"},
        ]

# Overide the theme colors
over_theme = {'txc_inactive': '#FFFFFF',
            #   'txc_active': '#31333F',
            #   'option_active': '#F0F2F6',
                'menu_background': '#31333F'
                }

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    home_name="Home",
    override_theme=over_theme,
    hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
    sticky_nav=False,  # at the top or not
    sticky_mode='Sticky',  # jumpy or not-jumpy, but sticky or pinned
    use_animation= False,
    )

if menu_id == "Home":
        apps.HomeApp()
elif menu_id == "Roadmap":
        apps.RoadmapApp()
elif menu_id == "Dashboard":
        apps.DashBoardApp()
elif menu_id == "Login":
        apps.LoginApp()
                  