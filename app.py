import streamlit as st
from PIL import Image
import cv2
from numpy import asarray

@st.cache
def load_image(img_file):
	img = Image.open(img_file)
	return img



def cartonize_image(our_image):
	new_img = asarray(our_image)
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	# Edges
	gray = cv2.medianBlur(gray, 5)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	#Color
	color = cv2.bilateralFilter(img, 9, 300, 300)
	#Cartoon
	cartoon = cv2.bitwise_and(color, color, mask=edges)

	return cartoon

st.title("Image Processing")

img_file = st.file_uploader("Upload tyre Images", type=['png','jpeg','jpg'])
 
if(img_file is not None):
	st.header("Original Image")
	st.image(load_image(img_file))
	st.header("Cartoon Image")
	st.image(cartonize_image(load_image(img_file)))
	
	 
  

