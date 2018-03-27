import os
import sys
import shutil

input = sys.argv[1]
filecount = 1


#列出輸入參數位置底下的文件
os.mkdir("YOLO")

for filename in os.listdir(input):
	os.system("E:\darknet\\build\darknet\\x64\darknet.exe detect cfg\yolov2.cfg weights\yolov2.weights " + input + "\\" + filename)
	os.rename("predictions.jpg", str(filecount) + ".jpg")
	shutil.move(str(filecount) + ".jpg","YOLO")
	filecount += 1
