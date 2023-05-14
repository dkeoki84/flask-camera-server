#! python
from flask import (
    Flask,
    render_template,
    Response
)
from app.camera import Camera

# init flask and camera
app = Flask(__name__)
cam = Camera()

# url to access main page
@app.route('/')
def index():
    return render_template('index.html')

# get camera image
def __gen__(cam: Camera):
    while True:
        frame = cam.get_frame()
        yield (
            b'--\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
        )

# url to access camera image
@app.route('/video_feed')
def video_feed():
    return Response(
        __gen__(cam),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
