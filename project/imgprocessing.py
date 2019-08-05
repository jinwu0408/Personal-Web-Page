import cv2
img = cv2.imread("img/IR-PCB.jpg",1)
image = cv2.resize(img,(610,680))
cv2.imwrite("img/IR-PCB.jpg",image)
