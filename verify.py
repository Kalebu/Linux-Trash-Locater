import os 
import hashlib
from PIL import Image


img_dir = [img for img in os.listdir() if img.endswith('jpg')]
'''
print("All images: ", len(img_dir))
img_unique_hashes =set([hashlib.sha256(Image.open(img).tobytes()).hexdigest() for img in img_dir])  
print("unique image : ", len(img_unique_hashes))
'''
img_hashes = []
count = 0

for index,  img in  enumerate(img_dir):
	img_id = Image.open(img).tobytes()
	img_hash = hashlib.md5(img_id).hexdigest()
	if img_hash in img_hashes:
		os.remove(img_dir[index])
		count+=1
		continue
	img_hashes.append(img_hash)

print('{} Duplicated image have been removed'.format(count))	

