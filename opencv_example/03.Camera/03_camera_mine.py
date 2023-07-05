import numpy as np
import cv2
# Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

topLeft = (50, 50)
bold = 0

sz = 0
r = 0
g = 0
b = 0


# Callback function for the trackbar
def on_bold_trackbar(value):
    #print("Trackbar value:", value)
    global bold
    bold = value

#크기 트랙바
def on_size_trackbar(val):
    global sz
    sz = val

#RGB trackbar
def r_trackbar(r_val):
    global r
    r = r_val

def g_trackbar(g_val):
    global g
    g = g_val

def b_trackbar(b_val):
    global b
    b = b_val


cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)

cv2.createTrackbar("size", "Camera", sz, 5, on_size_trackbar)
cv2.createTrackbar("red", "Camera", r, 255, r_trackbar)
cv2.createTrackbar("green", "Camera", g, 255, g_trackbar)
cv2.createTrackbar("blue", "Camera", b, 255, b_trackbar)


# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Text 
    cv2.putText(frame, "TEXT",
        (200,200), cv2.FONT_HERSHEY_SIMPLEX, 3+sz, (b, g, r), 1 + bold)


    # Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
