import streamlit as st
import pandas as pd
import numpy as np

import streamlit.components.v1 as components

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

speckle_var = {
    'Solar Irradiation':{
        'Annual':'rad/annual',
        'Summer':'rad/summer',
        'Spring':'rad/spring',
        'Winter':'rad/winter',
        },
    'Daylight':{
        'VSC':  'daylight/vsc',
        'DA':   'daylight/da',
        'DF':   'daylight/df', 
        'UDI':  'daylight/udi'
                },
    'Outdoor Comfort':{
        'Annual':'utci/annual',
        'Summer':'utci/summer',
        'Spring':'utci/spring',
        'Winter':'utci/winter',
        },
    'CFD':{
        '0':'cfd/0',
        '45':'cfd/45',
        '90':'cfd/90',
        '125':'cfd/125',
        '180':'cfd/180',
        '225':'cfd/225',
        '275':'cfd/275',
        '325':'cfd/325',
    }
}

######################################
# DASHBOARD SETTINGS
iframe_h = 500
st.set_page_config(layout="wide")

######################################
# HEADER

# company logo on top
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

# set 2 columns
col1, col2 = st.columns([2,1])

col1.markdown(""" 
# Hoare Lea Test Report V0.1
***Pablo Arango***

This a test case for showcasing the the great potential of web reporting utilizing **Python**,
**Speckle** and **Streamlit** for creating compeling web-based reports integrating 3D geometry as well as interactive plotting.
""")
st.write('---')


# col2.header('Project details')

project_details_df = pd.DataFrame(list(project_details.items()), columns=['Property', 'Value'])

# insert table second column
col2.table(project_details_df.astype(str))

######################################

# sidebar
st.sidebar.header('Set Speckle Stream ID')
SPECKLE_STREAM = st.sidebar.text_input('Speckle ID', '0b7b9e7705')


# sidebar
st.sidebar.header('Select Analysis Topic')

# select analysis type
sel_topic = st.sidebar.radio('Topic', ['Daylight', 'Solar Irradiation', 'Outdoor Wind Comfort', 'Outdoor Thermal Comfort', 'Air Quality'])

if sel_topic == 'Daylight':
    st.markdown("""
    ## Dayligthing
    Daylight in buildings is composed of a mix – direct sunlight, diffuse skylight, and light reflected from the ground and surrounding elements. Daylighting design needs to consider orientation and building site characteristics, facade and roof characteristics, size and placement of window openings, glazing and shading systems, and geometry and reflectance of interior surfaces. Good daylighting design ensures adequate light during daytime.""")

    sel_analysis = st.selectbox('Select Metric', ['VSC','DA', 'DF', 'UDI'])
    
    iframe_url = f"https://speckle.xyz/embed?stream={SPECKLE_STREAM}&branch={speckle_var[sel_topic][sel_analysis]}"
    iframe_url
    
    if sel_analysis == 'VSC':
        st.write("""
        ### Vertical Sky Component (VSC)
        The Building Research Establishment (BRE) have set out in their handbook ‘Site Layout Planning for Daylight and Sunlight a Guide to Good Practice (2011)’, 
        guidelines and methodology for the measurement and assessment of daylight and sunlight within proposed buildings. 
        One of the methods mentioned within section 2.1 and Appendix C of the handbook is the Vertical Sky Component (VSC).

        The VSC is a unit of measurement that represents the amount of available daylight from the sky, received at a particular window. It is measured on the outside face of the window. This unit is expressed as a percentage as it is the ratio between the amount of sky visible at the given reference point compared to the amount of light that would be available from a totally unobstructed hemisphere of sky. To put this unit of measurement into perspective, the maximum percentage value for a window with a completely unobstructed view through 90° in every direction is close to 50%. In order to maintain good levels of daylight the BRE guidance recommend that the VSC of a window should be 27% or greater. However, the 2011 BRE Handbook makes allowance for different target values in cases where a higher degree of obstruction may be unavoidable such as historic city centres or modern high rise buildings. *Source: BRE 2011*

        While most planning authorities now require these assessments, it is noted in the BRE Guidelines that they should be treated as guidelines as opposed to rules. 

        The guidelines state that if the VSC is:

        - **At least 27%**, then conventional window design will usually give reasonable results.
        - **Between 15% and 27%**, then special measures (larger windows, changes to room layout) are usually needed to provide adequate daylight.
        - **Between 5% and 15%**, then it is very difficult to provide adequate daylight unless very large windows are used.
        - **Less than 5%**, then it is often impossible to achieve reasonable daylight, even if the whole window wall is glazed
        """)

        components.iframe(iframe_url, height=iframe_h)
        
    elif sel_analysis == 'DA':
        st.write("""
        ### Daylight Autonomy [DA]
        Daylight autonomy (DA) is a daylight availability metric that corresponds to the percentage of the occupied time when the target 
        illuminance at a point in a space is met by daylight (Reinhart, 2001).
        
        A target illuminance of 300 lux and a threshold DA of 50%, meaning 50% of the time daylight levels are above the target illuminance, 
        are values that are currently promoted in the Illuminating Engineering Society of North America (IESNA, 2013), see section 1.9.4.
        
        Metrics: (WIP)
        - Average DA300
        - Mean DA300
        - Uniformity Dmin/Dav
        """)

        components.iframe(iframe_url, height=iframe_h)
        
    elif sel_analysis == 'DF':
        st.markdown("""
        ### Daylight Factor [DF]
        Daylight factor (DF) is a daylight availability metric that expresses as a percentage the amount of daylight available 
        inside a room (on a work plane) compared to the amount of unobstructed daylight available outside under overcast sky conditions (Hopkins,1963).
        The key building properties that determine the magnitude and distribution of the daylight factor in a space are (Mardaljevic, J. (2012)):

        - The size, distribution, location and transmission properties of the facade and roof windows.
        - The size and configuration of the space.
        - The reflective properties of the internal and external surfaces.
        - The degree to which external structures obscure the view of the sky.

        The higher the DF, the more daylight is available in the room. Rooms with an average DF of 2% or more can be considered daylit, but electric lighting 
        may still be needed to perform visual tasks. A room will appear strongly daylit when the average DF is 5% or more, in which case electric lighting 
        will most likely not be used during daytime (CIBSE, 2002).
        """)
        st.write('')
        components.iframe(iframe_url, height=iframe_h)
        
    elif sel_analysis == 'UDI':
        st.markdown("""
        ### Useful Daylight Illuminance [UDI]
        Useful daylight illuminance (UDI) is a daylight availability metric that corresponds to the percentage of the occupied time when a target range of 
        illuminances at a point in a space is met by daylight.

        Daylight illuminances in the range 100 to 300 lux are considered effective either as the sole source of illumination or in conjunction with 
        artificial lighting. Daylight illuminances in the range 300 to around 3 000 lux are often perceived as desirable (Mardaljevic et al, 2012).

        Recent examples in school daylighting design in the UK have led to recommendations to achieve UDI in the range 100-3 000 lux for 80% of occupancy hours.
        """)

        components.iframe(iframe_url, height=iframe_h)
        
elif sel_topic == 'Solar Irradiation':
    st.write("""
    ## Solar Irradiation
    Explain why solar irradiation is an important measure to follow
    - Solar energy gain
    - Overheating potential
    - Passive solar heating in winter
    - PV assessment
    """)
    
    sel_analysis = st.selectbox('Select Time Period', ['Annual','Summer', 'Spring', 'Winter'])
    
    # set dynamic iframe url    
    iframe_url = f"https://speckle.xyz/embed?stream={SPECKLE_STREAM}&branch={speckle_var[sel_topic][sel_analysis]}"
    iframe_url
    
    # display each analysis
    if sel_analysis == 'Annual':
        st.write("""
        ## Annual Analysis
        Something here
        """)
        
        components.iframe(iframe_url, height=iframe_h)

    elif sel_analysis == 'Summer':
        st.write("""
        ## Summer Analysis
        Typical summer day close to 21st of Jun
        """)

        components.iframe(iframe_url, height=iframe_h)

    elif sel_analysis == 'Spring':
        st.write("""
        ## Spring Analysis
        Typical spring day close to 21st of March
        """)
        
        components.iframe(iframe_url, height=iframe_h)
        
    elif sel_analysis == 'Winter':
        st.write("""
        ## Winter Analysis
        Typical winter day close to 21st of Dec
        """)
        
        components.iframe(iframe_url, height=iframe_h)
        
elif sel_topic == 'Outdoor Wind Comfort':
    st.warning('WIP')
    pass

elif sel_topic == 'Air Quality':
    st.warning('WIP')
    pass

elif sel_topic == 'Outdoor Comfort':
    st.warning('WIP')
    pass


