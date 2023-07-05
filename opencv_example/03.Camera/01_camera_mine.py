import numpy as np
import cv2

print(cv2.__version__)
# Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

w = 320#640#1280#1920
h = 240#480#720#1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

#카메라 input을 output.mp4로 저장
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output_file.mp4', fourcc, fps, (w,h))

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    # 우리 웹캠은 초당 30프레임이 디폴트.
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display
    cv2.imshow("Camera",frame)

    out.write(frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    

cap.release()
out.release() #output 동영상 내보내기...
cv2.destroyAllWindows()
