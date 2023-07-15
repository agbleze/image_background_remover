#%%
from image_background_changer import ImageBackgroundChanger
import joblib
import warnings
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import base64
import cv2
import numpy as np
import json
#%%
from PIL import Image
import io
from utils import decode_image

# def decode_image(encoded_image_string):
#     decoded_img = base64.b64decode(str(encoded_image_string))
#     img = Image.open(io.BytesIO(decoded_img))
#     img_array= cv2.cvtColor(np.array(img), cv2.IMREAD_COLOR)
#     return img_array

#%%

model_path = "model_store/model.h5"
app = Flask(__name__)

api = Api(app)

# develop flask api for image background remove
class ImageBackgroundRemover(Resource):
  @staticmethod
  def post():
    user_input = request.get_json()
    encoded_image = user_input['image']
    image = decode_image(encoded_image)

    blue_green_red_color = user_input['blue_green_red_color']

    img_bgrd_rm = ImageBackgroundChanger(image=image)
    model = img_bgrd_rm.load_model(model_path=model_path)
    preprocessed_img = img_bgrd_rm.image_preprocess()
    img_bgrd_rm.segment_image()
    image_with_background_changed = img_bgrd_rm.change_background_color(Blue_Green_Red_color=blue_green_red_color)
    #image_array_to_list = image_with_background_changed.tolist()
    #img_dump = json.dumps(image_with_background_changed.tolist())
    #new_background_json = {'processed_image': img_dump}#image_with_background_changed}
    return jsonify({'processed_image': image_with_background_changed.tolist()}) #new_background_json #jsonify(img_dump) #new_background_json #jsonify(new_background_json)
    

#   @staticmethod
#   def report():
#       return "working well"

api.add_resource(ImageBackgroundRemover, '/remove')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8012, debug=True)











# %%
