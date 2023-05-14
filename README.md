# flask-camera-server
Stream camera feed to web browser from flask server

## 1. Setup development environment
* Task 7 - Wrap up program inside a docker
* Task 1 - Capture Webcam Image data with OpenCV
* Task 2 - Stream Image Data In Webcam Browser GUI using flask

[Source reference](https://stackoverflow.com/questions/44852484/access-webcam-using-opencv-python-in-docker)

### **Task 7 - Wrap up program inside a docker**
```To enable easy collaboration for development and not to polute local system with software installs, we first dockerize the app.```

### **Task 1 - Capture Webcam Image data with OpenCV**
```Using the dockerized environment, implement a simple opencv camera capture app.```

### **Task 2 - Stream Image Data In Webcam Browser GUI using flask**
```Install flask on docker and stream opencv camera image to web browser.```

### **Problems 1**
#### Accessing host camera from inside docker
While dockerizing python and opencv on windows, was not able to access host camera and through some research, came upon an article on accessing host camera [here](https://medium.com/@jijupax/connect-the-webcam-to-docker-on-mac-or-windows-51d894c44468).

As macOs steps was easier to reproduce uing [Xquartz](https://gist.github.com/sorny/969fe55d85c9b0035b0109a31cbcb088), switched to develop on macOs but was still unable to get the camera access.

### **(Temporary) Solution 1**
#### Use debug frames to emulate camera frame access
```I believe if sufficient research and trial and error would fix this problem but, to complete the other (simple) tasks, I decide to emulate receiving camera frames from within the container and comeback to this problem after more research on the problem.```

## 2. Improve UI/UX
* Task 3 - Improve  the UI/UX
### **Task 3 - Improve the UI/UX**
Implement [bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) for fast UI improvements.
Add buttons for start/stop image streaming.

# running the app
## software requirements
* [Xquartz](https://formulae.brew.sh/cask/xquartz) (macOS m1) [setup](https://gist.github.com/sorny/969fe55d85c9b0035b0109a31cbcb088)
* [Docker](https://www.docker.com/products/docker-desktop/)
```bash
# In terminal type
docker-compose up
```
