import glob
import json


directory = "cake"

json_path = "./" + directory + "/info.json"

json_open = open(json_path, 'r')
d = json.load(json_open)
print(d)


