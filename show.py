
import os
import sys
import numpy as np
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from pycocotools import mask as maskUtils
 
from skimage import io
from matplotlib import pyplot as plt

CATEGORIES = [
        "__background",
        "plane",
        "baseball-diamond",
        "bridge",
        "ground-track-field",
        "small-vehicle",
        "large-vehicle",
        "ship",
        "tennis-court",
        "basketball-court",
        "storage-tank",
        "soccer-ball-field",
        "roundabout",
        "harbor",
        "swimming-pool",
        "helicopter",
        "container-crane"
    ]

 
def showDOTA(ROOT_DIR, ann="instances_DOTA_v1.5_train2018_add_difficult.json"): 
    coco = COCO(os.path.join(ROOT_DIR, ann))
    catIds = coco.getCatIds()
    imgIds = coco.getImgIds()
    img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]
    
    I = io.imread(os.path.join(ROOT_DIR, "images", img['file_name']))
    plt.axis('off')
    plt.imshow(I)
    # plt.show()
    # io.imsave(os.path.join(dataset_dir, img['file_name']), I)
    
    # bg = np.zeros((img['height'], img['width'], 3))
    # plt.imshow(bg)
    # plt.axis('off')
    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    # print(anns)
    print(img['id'])
    coco.showAnns(anns)
    plt.show()

if __name__ == "__main__":
    # Root directory of the project
    ROOT_DIR = '../demo/trainsplit_768_data'
    ann = "instances_DOTA_v1.5_train2018_add_difficult.json"
    showDOTA(ROOT_DIR,ann)
