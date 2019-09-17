import os 
import hashlib
from PIL import Image


class  Trash:
	def __init__(self):
		self.duplicated_img:list = []
		self.count_duplicated:int = 0

	def scrap_file_path(self, file_encoding:str = 'jpg')->list:
		command:str = 'locate {} >file_path.txt'.format(file_encoding)
		decode_selector = '.'+file_encoding+'\n'
		os.system(command)
		img_paths:str = [img.split('\n')[0] for img in open('file_path.txt', 'r+').readlines() if img.endswith(decode_selector)]
		return img_paths


	def Space_occupied(self, file_paths:str)->str:
		T_space:float = 0.0
		for file in file_paths:
			try:
				T_space+=os.path.getsize(file)
			except Exception as ex:
				#print(ex)
				print(0, end='')
		T_space = T_space//1048576
		return T_space 


	def investigate(self, file_paths:str)->list:
		unique_hashes:list = []
		repeated_hashes:list = []
		unique_paths:list = []
		repeated_paths:list = []
		for filename in file_paths:
			try:
				digital_hash:str = hashlib.md5(open(filename, 'rb').read()).hexdigest()
			except Exception as ex:
				#print(ex)
				print(0, end='')
				continue
			if digital_hash in unique_hashes:
				repeated_hashes.append(digital_hash)
				repeated_paths.append(filename)
				continue
			unique_hashes.append(digital_hash)
			unique_paths.append(filename)
		mined_summary:list = [[unique_hashes,self.Space_occupied(unique_hashes)], [repeated_hashes, self.Space_occupied(repeated_hashes)]]
		return mined_summary


	def remove_repeated(self, img_paths:list)->bool:
		for img in img_paths:
			try:
				os.remove(img)
			except Exception as ex:
				print(0, end='')
				continue
		return True

