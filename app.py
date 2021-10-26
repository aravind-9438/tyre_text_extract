import streamlit as st
from PIL import Image
import cv2
import numpy as np
from numpy import asarray
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\aravind reddy\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"  


st.set_page_config(
      page_title="Image processing",
      page_icon="tyre.jpg",
      layout="wide",
      initial_sidebar_state="expanded",
      menu_items={
          'Get Help': 'https://www.extremelycoolapp.com/help',
          'Report a bug': "https://www.extremelycoolapp.com/bug",
          'About': "# This is a header. This is an *extremely* cool app!"
      }
  )

@st.cache
def load_image(img_file):
	img = Image.open(img_file)
	return img

 

st.title("Image Processing")

img_file = st.file_uploader("Upload tyre Images", type=['png','jpeg','jpg'])

 


if(img_file is not None):
  img = load_image(img_file)
  custom_config = r'--oem 3 --psm 6'
  result = pytesseract.image_to_string(img, config=custom_config) 

  st.write(result)

	
	  


 



 

 