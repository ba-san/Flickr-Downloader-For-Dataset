# Flickr-Downloader-For-Dataset

## What's need to be fixed.

1.If there be " in a image title, json file will be corrupt.  
You need to fix them to add backslash just before " manually.  

2.If there be some Chinese characters, it is a possible to cause Character encoding error.  
In this case, you need to set a file in Python's 'site-packages'.  

## Instruction

1.You need to sign up to [flickr](https://www.flickr.com/) to get API keys.  

2.set up 'downloader.py' for downloading setting.  

3.setting 'multi-download.sh' for the time setting.  

4.run 'multi-download.sh'. You will get images and json files in chronological order.  

5.When you've removed some images in your folder, you need to run 'json_clearner.py' to amend a json file.  

## Reference
https://creativecommons.org/

https://itstudio.co/2018/12/28/8664/
(written in Japanese)
