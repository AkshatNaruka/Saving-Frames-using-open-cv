import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('x'):
        print("Exiting...")
        break

    elif cv2.waitKey(1) == ord('s'): 
            cv2.imwrite(filename='test.jpg', img=frame)
            cam.release()
            img_new = cv2.imread('test.jpg')
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")

        
            break

cam.release()
cv2.destroyAllWindows()
