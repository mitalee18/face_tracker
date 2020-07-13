import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            #puts rectangle on our face
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4) 

        cv2.imshow("My window", frame)

    # 1 is the frame rate which is 1 milli second, but 30 is fine
    key = cv2.waitKey(30) 

    #ord is to compare unicode value of 'q' with with the unicode value we get in key
    if key == ord("q"): 
        break #if q is pressed on keyboard it will quite

cap.release()
cv2.destroyAllWindows()