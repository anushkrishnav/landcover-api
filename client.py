data = '{"lat":"b","long":"k"}'
url=f'https://landcoverapi.azurewebsites.net/predict/{"lat":"b","long":"k"}'
import requests
import json

# files = {'image': open('1.3.png', 'rb')}
files='{"test":"sucess"}'
jsonData = json.dumps(files)
response = requests.request("POST", url)
print(response.text)