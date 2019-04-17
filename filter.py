import os
from tqdm import tqdm 
folder = '../demo/trainsplit_768_data'

img_list = sorted(os.listdir(os.path.join(folder, 'images')))
txt_list = sorted(os.listdir(os.path.join(folder, 'labelTxt_obb')))

for img, txt in tqdm(zip(img_list, txt_list)):
	img_path = os.path.join(folder, 'images', img)
	txt_path = os.path.join(folder, 'labelTxt_obb', txt)
	if os.path.getsize(txt_path) == 0:
		os.remove(txt_path)
		os.remove(img_path)

f_img_list = sorted(os.listdir(os.path.join(folder, 'images')))

print("total number:", len(img_list))
print("after remove:", len(f_img_list))
