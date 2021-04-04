data = '{"lat":"b","long":"k"}'
url=f'http://127.0.0.1:8000/predict/{data}'
import requests
import json

# files = {'image': open('1.3.png', 'rb')}
files='{"test":"sucess"}'
jsonData = json.dumps(files)
response = requests.request("POST", url)
print(response.text)