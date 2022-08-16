import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(f'v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=(int)3840, height=(int)2160 !  nvjpegdec ! video/x-raw, format=I420 ! appsink', cv2.CAP_GSTREAMER)
# Capture frame
ret, frame = cap.read()
if ret:
    cv2.imwrite('image1.jpg', frame)
cap.release()
