import base64
import requests
import json

class Communication:

    def __init__(self, url):
        self.url = url
    
    def set_url(self, url):
        self.url = url

    def post_image(self,image_name):

        with open(image_name, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        
        r = requests.post(f"{self.url}/xdxdxdxdx/png", data= encoded_string)

        print(r.text)