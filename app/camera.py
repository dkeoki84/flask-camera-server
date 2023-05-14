#! python

import cv2

# Class for camera
class Camera:

    # camera initialization
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        print(self.cam.isOpened())

    # get camera frame
    def get_frame(self):
        while True:
            success, frame = self.cam.read()
            if not success:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield frame
