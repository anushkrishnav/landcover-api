url="http://127.0.0.1:8000/predict/image"
import requests

files = {'image': open('your_image.png', 'rb')}

response = requests.request("POST", url, files=files)
print(response.text)