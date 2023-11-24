import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    image = Image.open("images/photo.JPG")
    rotated_image = image.rotate(90)
    st.image(rotated_image)

with col2:
    st.title("David Ramirez")
    content = """
    Summer 2023 projects from:
    Python Mega Course: Learn Python in 60 Days, Build 20 Apps

    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built with python. Feel free to contact me
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
