# Open CSI-Camera on Jetson
With Ubuntu 20

To compile:

```
$ g++ -std=c++11 -Wall -I/usr/lib/opencv -I/usr/include/opencv4 open_cam.cpp -L/usr/lib -lopencv_core -lopencv_highgui -lopencv_videoio -o open_cam
```
To run:

```
$ ./open_cam
```

OpenCV needs to be compiled with CUDA
