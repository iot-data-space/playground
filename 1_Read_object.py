import requests
import json

broker = "http://192.168.1.18:1026"
url = broker + "/ngsi-ld/v1/entities/"
#Read a building record
print("----Read a single object----")
url = url + "urn:milestone:camera1"
headers = {
  'Link':'<https://iot-data-space.github.io/context/context/milestone.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}
response = requests.request("GET", url, headers=headers)
building = json.loads(response.text)
print(json.dumps(building, indent=4))

