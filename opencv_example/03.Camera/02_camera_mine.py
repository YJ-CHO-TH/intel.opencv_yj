import numpy as np
import cv2
# Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

topLeft = (50, 50)
bottomRight = (300, 300)


#마우스 클릭하면 그곳에 동그라미 그려지게
point = (200, 200)
def click(event, x, y, flag, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("pressed", (x,y))
        point = (x,y)


# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Line
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)

    # Rectangle
    #cv2.rectangle(frame, 
    #    [pt+10 for pt in topLeft], [pt-10 for pt in bottomRight], (0, 50, 25), 5) 

    #circle
    cv2.circle(frame, point, 150, (88,33,22), 10)

    # Text 
    font = cv2.FONT_ITALIC
    cv2.putText(frame, 'suspect', [pt+80 for pt in topLeft], font, 2, (200, 15, 100), 5)

    # Display
    cv2.imshow("Camera",frame)



    cv2.setMouseCallback("Camera", click)


    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
