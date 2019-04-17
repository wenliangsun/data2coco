'''
convert the bounding boxes in txt form to binary mask pictures
'''
import os
import cv2
import numpy as np 
from skimage.io import imread, imsave
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

"""
数据格式:
dataname
  + images
  + labelTxt_obb
  + binary_mask

"""
# 数据的路径
set_name = '../demo/trainsplit_768_data'

image_path = os.path.join(set_name, 'images')
txt_ann_path = os.path.join( set_name,'labelTxt_obb')
store_ann = os.path.join(set_name,'binary_masks')

for file_idx in tqdm(os.listdir(txt_ann_path)):
    file_basename = os.path.splitext(file_idx)[0]
    img_file = os.path.join(image_path, file_basename+'.png')
    txt_file = os.path.join(txt_ann_path, file_idx)
    f = open(txt_file, 'r')
    objs = f.readlines()
    print("before filter",len(objs))
    objs = [obj.strip().split(' ') for obj in objs if obj.strip().split(' ')[-1]!='2']
#     print(objs)
    print("after filter",len(objs))
    num_objs = len(objs)
    
    im = cv2.imread(img_file)
    h, w, _ = im.shape

    for ix, obj in enumerate(objs):
        binary_mask = np.zeros((h, w), dtype=np.uint8)
        x1 = float(obj[0])
        y1 = float(obj[1])
        x2 = float(obj[2])
        y2 = float(obj[3])
        x3 = float(obj[4])
        y3 = float(obj[5])
        x4 = float(obj[6])
        y4 = float(obj[7])
        
        diff = obj[9]

        poly = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.int32)
        cls = obj[8]

        cv2.fillPoly(binary_mask, [poly], 255)
        imsave(os.path.join(store_ann, file_basename+'_'+cls+'_'+str(ix)+'.png'), binary_mask)
