import os 
from PIL import Image


class  ImageStudio:
	def __init__(self):
		self.duplicated_img:list = []
		self.count_duplicated:int = 0

	def scrap_img_path(self, img_encoding:str = 'jpg')->list:
		command:str = 'locate {} >img_path.txt'.format(img_encoding)
		os.system(command)
		img_paths:str = [img.split('\n')[0] for img in open('img_path.txt', 'r+').readlines()]
		return img_paths

	def create_img_hahes(self, img_paths:str)->list:
		unique_hashes:list = []
		repeated_hashes:list = []
		for img in img_paths:
			digital_hash:str = hashlib.md5(Image.open(img).tobytes()).hexdigest()
			if digital_hash in unique_hashes:
				se
