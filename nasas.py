import requests
key = "f1Ray4BvhkOMulelR1OQzJC92RPSiNHWpPyK3Yfi"
url = "https://api.nasa.gov/planetary/apod"
params = {'date' : '2021-04-04','api_key' : key,}
response = requests.request("GET",url=url)
print(response)
#'lat' : 13.0827,'long' : 80.2707