## https://itstudio.co/2018/12/28/8664/

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys, pathlib


def license_checker(num):
	if(num==0):
		return "All Rights Reserved"
	if(num==1):
		return "Attribution-NonCommercial-ShareAlike License"
	if(num==2):
		return "Attribution-NonCommercial License"
	if(num==3):
		return "Attribution-NonCommercial-NoDerivs License"
	if(num==4):
		return "Attribution License"
	if(num==5):
		return "Attribution-ShareAlike License"
	if(num==6):
		return "Attribution-NoDerivs License"
	if(num==7):
		return "No known copyright restrictions"
	if(num==8):
		return "United States Government Work"
	if(num==9):
		return "Public Domain Dedication (CC0)"
	if(num==10):
		return "Public Domain Mark"



# Your API Info.
key = "7c3138cf17ef1277b23aef6a62837875"
secret = "ec5f8543237296db"

wait_time = .8 # request span
imgname = sys.argv[1]
savedir = "./" + imgname
os.mkdir(savedir)

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
text = imgname, # search keyword
per_page = 5, # num of downloading img
media = 'photos',
license = '2,4,8,9,10',  # set licence id. # followd https://github.com/NVlabs/ffhq-dataset
sort = 'relevance',
safe_search = 1,
extras = 'license, url_o'
)

photos = result['photos'] # image info.

photos_str = str(photos)
photos_split = photos_str.split('{')

path_w = savedir + '/info.json'

with open(path_w, mode='w') as f:
	f.write('{')

for i, photo in enumerate(photos['photo']):
	
	try:
		url_o = photo['url_o']
		title = photo['title']
		width_o = photo['width_o']
		height_o = photo['height_o']
		info = flickr.photos.getInfo(photo_id=photo["id"])
		
		#print(info['photo'].keys()) # don't delete
		#print(info['photo']['tags']['tag'].keys()) # don't delete
		
		print("num:{}".format(i))
		print("\""+photo["id"]+"\":") # ID
		print("{\"url\":\""+info['photo']['urls']['url'][0]['_content']+"\",") # URL
		print("\"author\":\""+info['photo']['tags']['tag'][0]['authorname']+"\",") # Author
		print("\"title\":\""+title+"\",") # title
		print("\"license\":\""+str(license_checker(int(info['photo']['license'])))+"\",") # license
		print("\"original_width\":\""+str(width_o)+"\",") # original_width
		print("\"original_height\":\""+str(height_o)+"\"},\n") # original_height
	except:
		continue
	
	filepath = savedir + '/' + photo['id'] + '.jpg'
	
	# skip same file
	if os.path.exists(filepath): continue
	
	# download image
	urlretrieve(url_o,filepath)
	time.sleep(wait_time)
	
	with open(path_w, mode='a') as f:
		f.writelines("\""+photo["id"]+"\":") # ID
		f.writelines("{\"url\":\""+info['photo']['urls']['url'][0]['_content']+"\",") # URL
		f.writelines("\"author\":\""+info['photo']['tags']['tag'][0]['authorname']+"\",") # Author
		f.writelines("\"title\":\""+title+"\",") # title
		f.writelines("\"license\":\""+str(license_checker(int(info['photo']['license'])))+"\",") # license
		f.writelines("\"original_width\":\""+str(width_o)+"\",") # original_width
		f.writelines("\"original_height\":\""+str(height_o)+"\"},") # original_height


p_new = pathlib.Path(path_w)
s = p_new.read_text()
s = s[:-1] + "}"
p_new.write_text(s)
