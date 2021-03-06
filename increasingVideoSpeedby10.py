import cv2

videoCapture = cv2.VideoCapture("comp.avi")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter("MyOutput.avi", cv2.VideoWriter_fourcc("I","4", "2", "0"),(fps * 10), size)
success, frame = videoCapture.read()

#Write each frame.
while success:
    videoWriter.write(frame)
    success,frame = videoCapture.read()
