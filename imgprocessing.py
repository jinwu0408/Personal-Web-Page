import cv2
img = cv2.imread("images/logo.png",1)
image = cv2.resize(img,(225,225))
cv2.imwrite("images/logo.jpg",image)
