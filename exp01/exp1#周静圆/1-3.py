import cv2
import os
# 文件夹目录
path = r"D:\gitee\my_opencv\exps\exp01\images"
# 文件夹的所有文件名
files = os.listdir(path)
i = 1
# 遍历文件夹图片
for file in files:
    # 读取
    img = cv2.imread(path+"/"+file)
    cv2.imshow('window_title',img)
    # 图片改名
    name = '3035'+str(i)+'.jpg'
    # 保存
    cv2.imwrite(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    i = i + 1