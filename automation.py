import cv2 
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.videoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) +".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
        return image_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWIndows()

take_snapshot()
