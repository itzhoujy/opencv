import cv2

src = cv2.imread('puppy.jpg')
cv2.namedWindow("input",cv2.WINDOW_AUTOSIZE)
cv2.imshow('puppy',src)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
retval = cv2.imwrite("puppy.jpg",src)
cv2.destroyAllWindows()