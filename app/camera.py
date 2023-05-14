#! python

import cv2

# Class for camera
class Camera:

    # camera initialization
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    # get camera frame
    def get_frame(self):
        success, frame = self.cam.read()
        if not success:
            return None

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        return frame

    # for system debug
    FRAMES = [
        cv2.imread("./templates/static/red.png"),
        cv2.imread("./templates/static/green.png"),
        cv2.imread("./templates/static/blue.png")
    ]
    FRAME_LEN = len(FRAMES)
    frame_idx = 0
    def get_debug_frame(self):
        _, buffer = cv2.imencode('.jpg', self.FRAMES[self.frame_idx])
        frame = buffer.tobytes()

        # loop thru sample
        self.frame_idx += 1
        self.frame_idx %= self.FRAME_LEN

        return frame