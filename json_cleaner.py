import os
import glob
import json


directory = "cake"

json_path = "./" + directory + "/info.json"

json_open = open(json_path, 'r')
json_load = json.load(json_open)

json_list = json_load.keys()
json_delete_list = []

for json_file in json_list:
	filename = glob.glob("./" + directory + "/" + json_file + ".*")
	try:
		filename[0]
	except: # the case json's image is deleted in the folder
		json_delete_list.append(json_file) # also delete json information

for json_delete_file in json_delete_list:
	json_load.pop(json_file) # also delete json information

with open(json_path, 'w') as f:
    json.dump(json_load, f, ensure_ascii=False)


