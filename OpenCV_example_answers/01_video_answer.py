import numpy as np
import cv2

# Read from the recorded video file
cap = cv2.VideoCapture("ronaldinho.mp4")
#cap = cv2.VideoCapture("bb.avi")

idx = 0

# 동영상 파일이 성공적으로 열렸으면 while 문 반복
while(cap.isOpened()):
	# 한 프레임을 읽어옴
    ret, frame = cap.read()

    if ret is False:
        print("Can't receive frame (stream end?). Repeat ...")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize
    resized = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    # Display
    cv2.imshow("Video Out", resized)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(33)
    if key & 0xFF == ord('q'):
        break
    # 'c' 입력 시 frame save
    if key & 0xFF == ord('c'):
        cv2.imwrite("{0:03}.jpg".format(idx), frame)
        idx += 1

cap.release()
cv2.destroyAllWindows()