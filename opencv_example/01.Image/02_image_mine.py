import numpy as np
import cv2

# 이미지 파일을 Read 하고 Color space 정보 출력
color = cv2.imread("strawberry.jpg", cv2.IMREAD_COLOR)
#color = cv2.imread("strawberry_dark.jpg", cv2.IMREAD_COLOR)
print(color.shape)
height,width,channels = color.shape
cv2.imshow("Original Image",color)

# Color channel 을 B,G,R 로 분할하여 출력
# 오픈cv는 bgr 순서임.
b,g,r = cv2.split(color)
bgr_split = np.concatenate((b,g,r),axis=1)
cv2.imshow("BGR Channels",bgr_split)

# 색공간을 BGR 에서 HSV 로 변환
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)

#rgb로 다시 변환
rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
#rgb_split2 = np.concatenate((r,g,b), axis=1)
cv2.imshow("RGB", rgb)

#흑백으로 전환
gr = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
cv2.imshow("gray", gr)

cv2.waitKey(0)
cv2.destroyAllWindows()