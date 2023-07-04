import numpy as np
import cv2

# 이미지 파일을 Read
img = cv2.imread("my_input.jpg")

# Crop 300x400 from original image from (100, 50)=(x,y)
cropped = img[50:450, 100:400]

# Resize cropped image from 300x400 to 400x200
resized = cv2.resize(cropped, (400,200))

# 1.5배 scale up
scale_percent = 150 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
scale_up = cv2.resize(img, dim)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display all
cv2.imshow("Original", img)
cv2.imshow("Cropped image", cropped)
cv2.imshow("Resized image", resized)
cv2.imshow("Scale up image", scale_up)
cv2.imshow("Rotated image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
