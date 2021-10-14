import streamlit as st
from PIL import Image

@st.cache
def load_image(img_file):
	img = Image.open(img_file)
	return img

st.title("Image Processing")

img_file = st.file_uploader("Upload tyre Images", type=['png','jpeg','jpg'])
 
if(img_file is not None):
	st.image(load_image(img_file))

