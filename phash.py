#coding:utf-8
"""
author: Haddy Yang(杨仕航)
date: 2016-04-05
filename: opencv_phash.py
decription: pHash算法（感知哈希算法）实现
            把图片转成一个Hash值
测试环境：python2.7 win7 numpy1.11 OpenCV2.4.12
"""
#numpy是OpenCV必须的科学计算库
#OpenCV在Windows系统安装比较麻烦，下载OpenCV2.4的安装程序，执行会解压得到一个目录。
#打开目录build/python/2.7，复制里面的cv2.pyd文件到C:\Python27\Lib\site-packages中即可
import cv2
import cv2.cv as cv
import numpy as np

from compiler.ast import flatten
import sys

def pHash(imgfile):
	"""get image pHash value"""
	#加载并调整图片为32x32灰度图片
	img=cv2.imread(imgfile, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	img=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)

        #创建二维列表
	h, w = img.shape[:2]
	vis0 = np.zeros((h,w), np.float32)
	vis0[:h,:w] = img       #填充数据

	#二维Dct变换
	vis1 = cv2.dct(cv2.dct(vis0))
	#cv.SaveImage('a.jpg',cv.fromarray(vis0)) #保存图片
	vis1.resize(8,8)

	#把二维list变成一维list
	img_list=flatten(vis1.tolist()) 

	#计算均值
	avg = sum(img_list)*1./len(img_list)
	avg_list = ['0' if i<avg else '1' for i in img_list]

	#得到哈希值
	return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,64,4)])

if __name__ == '__main__':
	if len(sys.argv)!=2:
		print 'Error: args error, sample: opencv_phash 1.jpg'
	else:
		print pHash(sys.argv[1])
