# 生成coco格式数据(以DOTA数据集为例)

## 安装

```cd $INSTALL_DIR
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
python setup.py build_ext install
```

## 需要文件

+ pycococreator-master/pycococreatortools
+ filter.py
+ txt2mask.py
+ shapes_to_coco.py
+ show.py

##  执行顺序

+ 使用filter.py 文件过滤没有目标的图片
+ 使用txt2mask.py将txt标签转换成binary mask
+ 使用shapes_to_coco.py 生成coco格式的json标签



## 数据可视化

+ 使用show.py文件,可验证转换后的coco数据格式是否正确