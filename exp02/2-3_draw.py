import cv2
img = cv2.imread('puppy.jpg',1)
img = cv2.resize(img,(512,360))
cv2.imshow('puppy',img)
cv2.waitKey()

img = cv2.rectangle(img,(100,200),(200,300),(255,0,0),3)  # 绘制矩形
cv2.imshow('puppy',img)
cv2.waitKey()

img = cv2.circle(img,(250,356),23,(0,0,255),-1)  # 绘制圆形
cv2.imshow('puppy',img)
cv2.waitKey()

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'dogdogdog',(100,100),font,1.6,(0,0,255),2)  # 文本
cv2.imshow('puppy',img)

cv2.waitKey()
cv2.destroyAllWindows()