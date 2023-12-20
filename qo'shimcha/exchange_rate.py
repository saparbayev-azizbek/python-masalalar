import requests
import json
from pprint import pprint as print

sura = 1
oyat = 255
author = 'uzb-alauddinmansour'
url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{author}/{sura}/{oyat}.json'

r = requests.get(url)
data = r.json()['']
# Your JSON object
print(data['result'])