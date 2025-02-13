from pathlib import Path
from dotenv import load_dotenv
import requests
import json
import os

BASEDIR = Path(__file__).parent
load_dotenv(BASEDIR.joinpath(".env"), override=True)

broker = "http://192.168.1.18:1026"
objects = BASEDIR.joinpath("objects.json")

url = broker + "/ngsi-ld/v1/entities/"

headers = {
  'Content-Type': 'application/ld+json'
}

with open(objects, 'r') as file:
    objects = json.load(file)

print("NGSI-LD Post at " + broker)
for payload in objects:
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(response.text)