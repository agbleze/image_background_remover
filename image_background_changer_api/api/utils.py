import requests
import json
import numpy as np
import base64
from PIL import Image
import io
import cv2

# func to make request to background remover api

def request_image_background_change(data: dict, URL: str = None,) -> int:
    """
    This function makes an API request to the image background change API
    and returnsan image with the changed to what user requested

    Parameters
    ----------
    URL : Endpoint of image background color change API
        The API link.
    data : dict
        input data to be used for prediction. This should be a dictionary
        composed of image and color to change image background to.
        keys as image and blue_green_red_color
        image: image whose background is to be changed

        blue_green_red_color: Background color to change image background to.
          This is a list of pixel values (intergers) ideally in the range of 0 - 255
    Returns
    -------
    NdArray
        Image.

    """
    req = requests.post(url=URL, json=data)
    response = req.content
    #print("Processed image successfully returned from API")
    #print("... Processing the response...")
    #prediction = json.loads(response)['processed_image']#[0]
    response_loaded = json.loads(response)
    response_processed_img_list = response_loaded['processed_image']
    response_processed_img_array = np.array(response_processed_img_list)
    return response_processed_img_array
    


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

def decode_image(encoded_image_string):
    decoded_img = base64.b64decode(str(encoded_image_string))
    img = Image.open(io.BytesIO(decoded_img))
    img_array= cv2.cvtColor(np.array(img), cv2.IMREAD_COLOR)
    return img_array
