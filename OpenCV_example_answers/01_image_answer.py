import numpy as np
import cv2

# 이미지 파일을 Read
img = cv2.imread("my_input.jpg")

# Image 란 이름의 Display 창 생성
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# Numpy ndarray H/W/C order
print(img.shape)

# Read 한 이미지 파일을 Display
cv2.imshow("image", img)

# 별도 키 입력이 있을때 까지 대기하고 입력된 key 값을 저장
key = cv2.waitKey(0)

# 입력된 key 값이 's' 일 경우 output.png 로 읽은 이미지 파일을 저장
if key == ord('s'):
    cv2.imwrite("output.png", img)

# Destroy all windows
cv2.destroyAllWindows()
