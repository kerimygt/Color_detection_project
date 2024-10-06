import cv2 as cv
from util import get_limits
from PIL import Image

webcam = cv.VideoCapture(0)

yellow = [0, 255, 255]

while True:
    ret, frame = webcam.read()

    hsv_img = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)

    mask = cv.inRange(hsv_img,lower_limit,upper_limit)
    
    mask = Image.fromarray(mask)
    bbox = mask.getbbox()

    #print(bbox)
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame,(x1,y1),(x2 ,y2),(0,255,0),5)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv.destroyAllWindows()