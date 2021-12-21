import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('./xml/face.xml')

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
