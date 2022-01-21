import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

'_This_ is some **Markdown***'

st.text('Fixed width text')
st.markdown('_Markdown_', unsafe_allow_html = True) # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3], unsafe_allow_html = True) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')


## DISPLAY DATA

# st.dataframe(my_dataframe)
# st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric('My metric', 42, 2)

## ADD WIDGETS TO THE SIDEBAR

a = st.sidebar.radio('Select one:', [1,2])

with st.sidebar:
    st.radio('Select anotherone:', [3,4])

## COLUMNS
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Different sizes
cols= st.columns([3, 1, 1])

for i ,col in enumerate(cols):
    col.write('This is column {}'.format(i))

with col1:
    st.radio('Select third:', [1,2])

## CONTROL FLOW

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')

## INTERACTIVE WIDGETS

st.button('Click me') # bool
st.checkbox('I agree') # bool
st.radio('Pick one', ['cats', 'dogs']) # item
st.selectbox('Pick one', ['cats', 'dogs']) # item
st.multiselect('Buy', ['milk', 'apples', 'potatoes']) # list
st.slider('Pick a number', 0, 100)
st.text_input('First Name:')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a photo')
# st.download_button('Download a file', data)
st.color_picker('Pick a color')

# for i in range(int(st.number_input('Num:'))):
#   foo()
# if st.sidebar.selectbox('I:',['f']) == 'f':
#   b()
# my_slider_val = st.slider('Quinn Mallory', 1, 88)
# st.write(slider_val)

with st.echo():
  st.write('Code will be executed and printed')

