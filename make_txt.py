# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 16:38
# @Author  : Michael
# @File    : make_txt.py
# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*
import os
import random
# '''
# 训练验证：测试=0.8：0.2
# 训练验证中   训练：验证 = 0.75：0.25
# 总 6：2：2
# '''
trainval_percent = 0.8  #训练和验证
train_percent = 0.75
xmlfilepath = 'data/Annotations'
txtsavepath = 'data/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)  #统计所有的标注文件
list = range(num)
tv = int(num * trainval_percent)  # 设置训练验证集的数目
tr = int(tv * train_percent)      # 设置训练集的数目

trainval = random.sample(list, tv)
train = random.sample(trainval, tr)


# txt 文件写入的只是xml 文件的文件名（数字），没有后缀，如下图。
ftrainval = open('data/ImageSets/Main/trainval.txt', 'w')
ftest = open('data/ImageSets/Main/test.txt', 'w')
ftrain = open('data/ImageSets/Main/train.txt', 'w')
fval = open('data/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()




