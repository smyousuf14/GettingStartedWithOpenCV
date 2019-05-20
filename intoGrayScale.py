#Converts a jpeg image into a gray-scale png image
import cv2
grayImage = cv2.imread("scene.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("scene.png",grayImage)
