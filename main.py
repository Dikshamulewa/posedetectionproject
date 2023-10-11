import cv2 as cv
from cvzone.PoseModule import PoseDetector

video = cv.VideoCapture(0)
pd = PoseDetector()

while True:
    ret,img = video.read()
    img = pd.findPose(img)
    lmlist,bbox = pd.findPosition(img)
    print(lmlist)

    cv.imshow('frame',img)
    key = cv.waitKey(10)
    if key == 27 :
        cv2.destroyAllWindoes()
        break