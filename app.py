#! python
from flask import (
    Flask,
    render_template,
    Response,
    request
)
from app.camera import Camera

# DEBUG
debug = True

# init flask and camera
app = Flask(__name__)
cam = None
def get_cam():
    global cam
    if cam:
        return cam

    cam = Camera()
    return cam

# url to access main page
@app.route('/')
def index():
    return render_template('index.html')

# get camera image
def __gen__(cam: Camera):
    global debug
    while True:
        frame = cam.get_debug_frame() if debug else cam.get_frame()
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
        )

# url to access camera image
@app.route('/video_feed')
def video_feed():
    global cam
    return Response(
        __gen__(get_cam()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# contrast control
@app.route('/contrast', methods=["POST"])
def contrast():
    data = request.get_json()
    contrast = float(data["val"])
    get_cam().set_contrast(contrast)
    return "", 200

# brightness control
@app.route('/brightness', methods=["POST"])
def brightness():
    data = request.get_json()
    brightness = int(data["val"])
    get_cam().set_brightness(brightness)
    return "", 200

# main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
