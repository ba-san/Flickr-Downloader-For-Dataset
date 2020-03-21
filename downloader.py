from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys, pathlib

def license_checker(num):
	if(num==0): return "All Rights Reserved"
	if(num==1): return "Attribution-NonCommercial-ShareAlike License"
	if(num==2): return "Attribution-NonCommercial License"
	if(num==3): return "Attribution-NonCommercial-NoDerivs License"
	if(num==4): return "Attribution License"
	if(num==5): return "Attribution-ShareAlike License"
	if(num==6): return "Attribution-NoDerivs License"
	if(num==7): return "No known copyright restrictions"
	if(num==8): return "United States Government Work"
	if(num==9): return "Public Domain Dedication (CC0)"
	if(num==10): return "Public Domain Mark"

# Your API Info. Get from here. https://www.flickr.com/services/api/
key = "input_your_key_here"
secret = "input_your_secret_key_here"

wait_time = 1 # request span. Recommended not to change it.
imgname = sys.argv[1]
savedir = "./" + imgname
path_w = savedir + '/' + os.path.basename(savedir) + '_info.json' # image information will be written to this json file.
os.mkdir(savedir)

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
#text = imgname, # search keyword
text = "crowd night", # search keyword
per_page = 500, # num of downloading img. max is 500
media = 'photos',
min_upload_date = '2032-03-01',
max_upload_date = '2032-04-30',
license = '2,4,9,10',  # set licence id.
sort = 'relevance', # 'relevance' is good option
extras = 'license, url_o'
)

photos = result['photos'] # image info.
photos_str = str(photos)
photos_split = photos_str.split('{')

with open(path_w, mode='w') as f:
	f.write('{')

for i, photo in enumerate(photos['photo']):
	try:
		url_o = photo['url_o']
		title = photo['title']
		width_o = photo['width_o']
		height_o = photo['height_o']
		info = flickr.photos.getInfo(photo_id=photo["id"])

		#print(photo)
		#print(info['photo'].keys())
		#print(info['photo']['tags']['tag'].keys())
		
		print("num:{}".format(i))
		print("\""+photo["id"]+"\":") # ID
		print("{\"url\":\""+info['photo']['urls']['url'][0]['_content']+"\",") # URL
		print("\"author\":\""+info['photo']['tags']['tag'][0]['authorname']+"\",") # Author (username is better?)
		print("\"title\":\""+title+"\",") # title
		print("\"license\":\""+str(license_checker(int(info['photo']['license'])))+"\",") # license
		print("\"original_width\":\""+str(width_o)+"\",") # original_width
		print("\"original_height\":\""+str(height_o)+"\"},\n") # original_height
		
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
		
	except:
		continue


p_new = pathlib.Path(path_w)
s = p_new.read_text()
s = s[:-1] + "}"
p_new.write_text(s)
