
import sys
sys.stdin=open("cv2.jpg", "w")
from sketchpy import canvas

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressedz
        img_name = "opencv_frame.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break
cv2.destroyAllWindows()
object = canvas.sketch_from_image("opencv_frame.png".format(img_counter))
object.draw()
cam.release()

cv2.destroyAllWindows()