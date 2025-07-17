from PIL import Image
import streamlit as st
st.set_page_config(page_title="CdxGD", page_icon="images/icon.png", layout="wide")
img_contact_form = Image.open("images/icon.png")
img_contact_form = Image.open("images/my_icon.png")
st.title("This is the official website of Lihencdxx")
image_column,text_column = st.columns((1, 2))
with image_column:
    st.image("images/my_icon.png")
st.write("This is the official website of Lihencdxx and you will see other stuff from me here")
st.write("[official youtube](https://www.youtube.com/@LIHENCDXXGD)")
st.write("---")
st.write("I am Lihencdxx and I will be a future top player")
st.write("heres some information about me")
st.write("Hardest: [Nine circles](https://youtu.be/AlUhrSyc8I4?si=ufzVlyA9B4_W0yTD):")
st.write("Level working on: xo [hardest run](https://youtu.be/6K6erwf4FRk?si=SaCnHFaYvvqbbk7R)")