import streamlit as st
from PIL import Image
import cv2
import numpy as np
from numpy import asarray
import easyocr as ocr

 

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

 
@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader

st.title("Image Processing")

img_file = st.file_uploader("Upload tyre Images", type=['png','jpeg','jpg'])

 
reader = load_model()

if(img_file is not None):
	img = load_image(img_file)
	
	with st.spinner("🤖 AI is at Work! "):
		result = reader.readtext(np.array(img))
		result_text = ''  
		p = []
		for text in result:
 
			if(text[-1]>0.6):
				result_text += [text[1],text[-1]]
				p.append(text[-1])
 
			 
	st.write(result_text)
	st.write(sum(p)/len(p))
	
	st.balloons()
 
	

	
	  


 



 

 
