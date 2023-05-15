#! python

import cv2
from datetime import datetime

# Class for camera
class Camera:
    OPT_RENDER_TIME = "time"

    # camera initialization
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        
        # emulate contrast & brightness
        self.contrast = 0.5     # range 0 < x < 1
        self.brightness = 0     # range -127 < x < 127

        # render options
        self.options = {
            self.OPT_RENDER_TIME: 0
        }

    # emulate camera contrast & brightness
    def __process_contrast_brightness(self, frame):
        cv2.convertScaleAbs(frame, self.contrast, self.brightness)

    # execute image process
    def __process_image(self, frame):
        key = self.OPT_RENDER_TIME
        if self.options[key]:
            self.__process_time_render(frame)
        
        # other image process...

    def __process_time_render(self, frame):
        date = datetime.now()
        frame = cv2.putText(
            frame,
            str(date),
            (8, 32),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

    def set_contrast(self, contrast):
        self.contrast = contrast

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_render(self, options):
        key = self.OPT_RENDER_TIME
        if key in options:
            self.options[key] = options[key]

    # get camera frame
    def get_frame(self):
        success, frame = self.cam.read()
        if not success:
            return None

        self.__process_contrast_brightness(frame)
        self.__process_image(frame)

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
        frame = self.FRAMES[self.frame_idx].copy()
        self.__process_contrast_brightness(frame)
        self.__process_image(frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # loop thru sample
        self.frame_idx += 1
        self.frame_idx %= self.FRAME_LEN

        return frame
