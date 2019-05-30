import cv2

def detect():
    stop_cascade = cv2.CascadeClassifier("./cascades/stop_sign.xml")
    camera = cv2.VideoCapture(0)

    while(True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        stop_signs = stop_cascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in stop_signs:
            img = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
            print("Stop Sign Detected with Height of " + str(h) + " and width of " + str(w))

        cv2.imshow("camera", frame)
        if cv2.waitKey(83) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


detect()
