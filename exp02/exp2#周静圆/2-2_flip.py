import cv2

img = cv2.imread('puppy.jpg')
img = cv2.resize(img,(256, 150))
cv2.imshow('puppy',img)

img_flip_v = cv2.flip(img,0)  # 0代表垂直翻转
cv2.imshow('puppy_flip_v',img_flip_v)  # 显示图片

img_flip_h = cv2.flip(img,1)  # 1代表水平翻转
cv2.imshow('puppy_flip_h',img_flip_h)  # 显示图片

cv2.waitKey()
cv2.destroyAllWindows()