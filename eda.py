import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import seaborn as sns

def run():
    # Membuat Title 
    st.title('EDA FIFA 2022')

    # Membuat Subheader
    st.subheader('Page ini dibuat oleh *Danu Purnomo*')

    # Menambahkan Teks
    st.write('# Teks 1')
    st.write('## Teks 2')

    # Menambahkan Gambar
    image_data = Image.open('./soccer.jpg')
    st.image(image_data, caption='EDA FIFA 2022')

    # Menambahkan DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # Menambahkan Plot
    st.write('## Histogram of Rating')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig)

    # Menambahkan Plot Sesuai dengan Input User
    st.write('## Histogram berdasarkan input user')
    opsi = st.selectbox('Column', ('Age', 'Height', 'Weight', 'ShootingTotal'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('## Plotly Plot - Overall vs ValueEUR')
    fig = px.scatter(df, x='ValueEUR', y='Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)


if __name__ == '__main__':
    run()