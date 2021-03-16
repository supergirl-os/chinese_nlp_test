import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# 禁用警告
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("可视化分析")
filename= 'texts/test1_cut.txt'
with open(filename,encoding='utf-8') as f:
    mytext=f.read()
wc1=WordCloud(background_color='white').generate(mytext)
plt.imshow(wc1,interpolation='bilinear')
plt.axis('off')
st.pyplot()