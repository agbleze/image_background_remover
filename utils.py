import requests
import json

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
    prediction = json.loads(response)['processed_image'][0]
    return prediction




