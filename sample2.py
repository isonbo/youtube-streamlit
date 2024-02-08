# 実行はVSC内のターミナルを開いて'streamlit run main.py'
# コマンド一覧：Welcome to Streamlit -> REFERENCE GUIDES -> API reference
# https://docs.streamlit.io/library/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')


st.write('Disply Image')

if st.checkbox('Show Image'):
  img = Image.open('切断部.PNG')
  st.image(img, caption='切断部', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は ', option, 'です'

st.write('Interactive Widgets')

# text = st.text_input('あなたの趣味を教えてください。')
text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition
