#%%
from utils import request_image_background_change
from PIL import Image

#%%

lin_img = Image.open('Linus_Pic.jpeg')

#%%

lin_img
URL = "http://192.168.0.168:8080/predict"

DEF_URL = "http://127.0.0.1:8010/remove_background"

data_json = {"image": lin_img, "blue_green_red_color": [123, 213, 231]}
#%%
import base64


#%%

import base64
image_path = "Linus_Pic.jpeg"
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

#%%
    
#%%

encoded_string.decode('utf-8')

#%%
import cv2

#%%
img = cv2.imread('Linus_Pic.jpeg', cv2.IMREAD_COLOR)


#%%

#img_list = img.tolist()


#%%



#%%

data_json = {"image": encoded_string.decode('utf-8'), "blue_green_red_color": [123, 213, 231]}


#%%
data_json = {"image": encoded_string.decode('utf-8'), 
             "blue_green_red_color": [123, 213, 231]
             }


#%%

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

#%%
def create_request_data(img_path, blue_green_red_color, 
                        encode_img_func = encode_image
                        ):
    request_image = encode_img_func(image_path=img_path).decode('utf-8')
    data_json = {"image": request_image, 
                "blue_green_red_color": blue_green_red_color
                }
    return data_json
    
#%%


create_request_data(img_path='Linus_Pic.jpeg', 
                    blue_green_red_color=[123, 213, 231]
                    )    
    
#%%

img_ext = data_json["image"]

#%%

img_resume = base64.b64decode(img_ext)

#%%
#cv2.imread(img_resume, cv2.IMREAD_COLOR)

#%%
import numpy as np
import io

#%% Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.IMREAD_COLOR)
    return opencv_img 


## to be used in the api
def decode_image(encoded_image_string):
    decoded_img = base64.b64decode(str(encoded_image_string))
    img = Image.open(io.BytesIO(decoded_img))
    img_array= cv2.cvtColor(np.array(img), cv2.IMREAD_COLOR)
    return img_array 


#%%

encode_image(img_rgb)

    
    
    
#%%

img_rgb = stringToRGB(img_ext)

#%%
import matplotlib.pyplot as plt

#%%

plt.imshow(img_rgb)
plt.show()

#%%
encode_image(img_rgb)

    

#%%
from flask import jsonify
new_background_json = {'processed_image': img_rgb}
jsonify(new_background_json)

#%%

#cv2.imshow('trial img',img_rgb)

#%%



#%%


request_image_background_change(data=data_json, URL=DEF_URL)


# %%
