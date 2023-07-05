import numpy as np
import cv2

# 이미지 파일을 Read
img = cv2.imread("ein.jpg")

# Crop 300x400 from original image from (100, 50)=(x,y)
print("img", img.shape)
cropped = img[70:250, 200:360]

# Resize cropped image from 300x400 to 400x200
resized = cv2.resize(cropped, (500,200))


scale_percent = 150
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width, height)
scale_up = cv2.resize(img, dim)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)



# Display all
#cv2.imshow("Original", img)
#v2.imshow("Cropped image", cropped)
#cv2.imshow("Resized image", resized)
#cv2.imshow("Scale up image", scale_up)
#cv2.imshow("Rotated image", rotated)




#마우스 클릭하면 그곳에 동그라미 그려지는건 안되지만
#눌린 포인트의 좌표가 print 됨
#img.shape 하면 (height, width, channels) 순서로 출력됨
point = (200, 200)
def click(event, x, y, flag, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("pressed", (x,y))

cv2.imshow("Original", img)
cv2.setMouseCallback("Original", click)




#s를 누르면 저장
key = cv2.waitKey(0)
if key == ord('s'): cv2.imwrite("ein_up.jpg", scale_up)


cv2.destroyAllWindows()
