import cv2
def takeSnapshot():
    videoCapture = cv2.VideoCapture(0)
    result = True 
    while (result):
        ret, frame = videoCapture.read()
        #a,b = 0
        cv2.imwrite("picture.jpg", frame)
        result = False
    videoCapture.release()
    cv2.destroyAllWindows()
takeSnapshot()