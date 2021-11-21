import streamlit as st
from PIL import Image
import cv2
import numpy as np
from numpy import asarray
import easyocr as ocr

 

 
@st.cache
def load_image(img_file):
	img = Image.open(img_file)
	return img

 
@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader

st.title("Tyre Text Extraction")

img_file = st.file_uploader("Upload tyre Images", type=['png','jpeg','jpg'])

 
reader = load_model()



if(img_file is not None):
	img = load_image(img_file)

	max_val=255
	kernal = np.ones((3,3), np.uint8)
	erosion = cv2.erode(np.array(img), kernal, iterations=1)
	guassian = cv2.GaussianBlur(erosion, (5,5),cv2.BORDER_DEFAULT)
	# _,t = cv2.threshold(guassian, 90, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU )

	
	with st.spinner("🤖 AI is at Work! "):
		result = reader.readtext(np.array(img))
		result_text = ''  
		p = []
		for text in result:
 
			if(text[-1]>0.6):
				result_text += text[1]
				p.append(text[-1])
 
		p = (sum(p)*100)//len(p)

	st.image(img,width=250,caption="Original image")
	st.image(guassian,width=250,caption="Guassian image")	 
	st.success("Predicted text: "+ result_text)
	st.write("Accuracy: " + str(p) + "%")
	
	st.balloons()
 
	

	
	  


 



 

 
