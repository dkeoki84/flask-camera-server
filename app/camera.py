#! python

import cv2

# Class for camera
class Camera:

    # camera initialization
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        
        # emulate contrast & brightness
        self.contrast = 0.5     # range 0 < x < 1
        self.brightness = 0     # range -127 < x < 127

    # emulate camera contrast & brightness
    def __process_contrast_brightness(self, frame):
        cv2.convertScaleAbs(frame, self.contrast, self.brightness)

    def set_contrast(self, contrast):
        self.contrast = contrast

    def set_brightness(self, brightness):
        self.brightness = brightness

    # get camera frame
    def get_frame(self):
        success, frame = self.cam.read()
        if not success:
            return None

        self.__process_contrast_brightness(frame)

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
        frame = self.FRAMES[self.frame_idx]
        self.__process_contrast_brightness(frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # loop thru sample
        self.frame_idx += 1
        self.frame_idx %= self.FRAME_LEN

        return frame