import streamlit as st
import numpy as np
import pandas as pd

st.title('title 1')

# show text
st.header('this is a header')
st.subheader('this is a sub header')
st.text('this is a normal text')
st.caption('this is caption')
# split line
st.divider()

# Markdown
st.markdown('# heading 1')
st.markdown('## heading 2')
st.markdown('### heading 3')
st.divider()


# link
st.markdown('click here [AIVN](http:link)')
# doc string
st.markdown("""
1. muc 1
2. muc 2
3. muc 3            
""")
st.divider()

# math fomular format
st.markdown(r"$\sqrt{2x-2}$")
# latex format
st.latex(r"\sqrt{2x+2}")
st.divider()

# code
st.code(
"""
import numpy as np
arr = np.arr([1,2,3])
"""
)
st.divider()


# show code, text, fomular
st.write('### heading 4')
st.write(r"$\sqrt{2x-2}$")

# debug in terminal
print('log chi hien thi o terminal')
st.divider()

# show media
st.logo('./assets/ChatGPT_Logo.png')
st.image('./assets/chibi1.png', caption = 'quang chibi')
st.divider()
st.audio('./assets/silent.wav')
st.divider()
st.video('./assets/Video_Mèo_Chibi_Dễ_Thương.mp4')
st.divider()

# input

# check box
status = st.checkbox('i agree')
st.write(f"status is: {status}")
st.divider()

# option
status = st.radio(
    'color:',
    ['Red','Blue','Green'],
    captions = ['chon mau do','chon mau xanh','chon mau blue']
    )
st.write(f'u color is {status}')
st.divider()

# select box
status = st.selectbox('contact',('mail','num','address'))
st.write(f'u choose {status}')
st.divider()

# multi select
status = st.multiselect(
    'colors:', [
        'green',
        'red',
        'pink',
        'blue'
    ]
)
st.write(f'u choose {status}')
st.write(status)
st.divider()

# slider

# distinct values
status = st.select_slider(
    'number: ',
    options = [2,4,6,8]
)
st.write(f'u choose {status}')

# choose 1 in range values
status = st.slider(
    'values',
    1.0,10.0
)
st.write(f'u choose {status}')
st.divider()

# choose range value
values = st.slider(
    'select rangde of value',
    0.0, 100.0, (25.0, 75.0)

)
st.write(values)
st.divider()

# text input
name = st.text_input('your name: ')
st.write(f'hi {name}')

# number input
num = st.number_input('u age: ')
st.write(f'wow, {num} noi banh trung')
st.divider()

# button
res = st.button('yeu khong')
st.write('yeu' if res else 'khong yeu')
st.divider()

# link button
st.link_button(
    'fanpage',
    'http://'
    )
st.divider()

# chatbot

#chat input
query = st.chat_input('say sth...')
st.write(f'just enter: {query}')
st.divider()

# upload file
file = st.file_uploader(
    'choose file'
)
st.divider()

# upload multiple file
files = st.file_uploader(
    'choose many file',
    accept_multiple_files = True
)
for file in files:
    st.write(file.name)
st.divider()

# chart
chart_data = pd.DataFrame(
    np.random.randn(10,3),
    columns = ['a','b','c']
)
st.bar_chart(chart_data)
st.divider()

