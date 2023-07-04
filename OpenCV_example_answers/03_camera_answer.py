import numpy as np
import cv2
# Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

topLeft = (0, 300)
bold = 0
fontsize = 0
R,G,B = 0,0,0

# Callback function for the trackbar
def on_bold_trackbar(value):
    global bold
    bold = value
def on_fontsize_trackbar(value):
    global fontsize
    fontsize = value
def on_R_trackbar(value):
    global R
    R = value
def on_G_trackbar(value):
    global G
    G = value
def on_B_trackbar(value):
    global B
    B = value

cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)
cv2.createTrackbar("size", "Camera", fontsize, 10, on_fontsize_trackbar)
cv2.createTrackbar("R", "Camera", R, 255, on_R_trackbar)
cv2.createTrackbar("G", "Camera", G, 255, on_G_trackbar)
cv2.createTrackbar("B", "Camera", B, 255, on_B_trackbar)

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Text 
    cv2.putText(frame, "TEXT",
        topLeft, cv2.FONT_HERSHEY_SIMPLEX, 1 + fontsize, (B, G, R), 1 + bold)

    # Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
