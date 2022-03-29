# -*- coding: utf-8 -*-
# @Time     : 12/13/21 8:57 PM

#将test.txt图片路径读取，放入data/samples
import shutil
import cv2
print('测试集导入')
ft = open('data/test.txt', 'r')
paths = [x.strip() for x in ft.read().splitlines() if len(x.strip())]
for path in paths:
    name = path.split("/")[-1]
    new_path = 'data/samples/' + name
    shutil.copy(path, new_path)
