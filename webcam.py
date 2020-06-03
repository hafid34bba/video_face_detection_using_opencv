import cv2
frameWidth = 640
frameHight = 480
faceCascade = cv2.CascadeClassifier("Images/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("put the path of your video or tap 0 if you want to use the webcam")
cap.set(3,frameWidth)
cap.set(4,frameHight)
cap.set(10,130)
while True:
    succes , img= cap.read()
    if succes==False:
        break
    imgResise = cv2.resize(img, (500,400))
    imgGray = cv2.cvtColor(imgResise, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgResise, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(imgResise, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.imshow('video', imgResise)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break