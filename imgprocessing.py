import cv2
img = cv2.imread("images/micromouse.jpg",1)
image = cv2.resize(img,(960,540))
cv2.imwrite("images/micromouse.jpg",image)
