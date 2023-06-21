#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;


string gstreamer_pipeline (int capture_width, int capture_height, int display_width, int display_height, int framerate, int flip_method) {

    return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)" + to_string(capture_width) + ", height=(int)" +
           to_string(capture_height) + ", framerate=(fraction)" + to_string(framerate) +
           "/1 ! nvvidconv flip-method=" + to_string(flip_method) + " ! video/x-raw, width=(int)" + to_string(display_width) + ", height=(int)" +
           to_string(display_height) + ", format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";
}

int main() {

    cout << "OpenCV version: " << CV_VERSION << endl;
    cout << "____________________________""\n";

    int capture_width  = 800;
    int capture_height = 600;
    int display_width  = 800;
    int display_height = 600;
    int framerate      = 30;
    int flip_method    = 0;

    Mat img;

    string pipeline = gstreamer_pipeline(capture_width,
	capture_height,
	display_width,
	display_height,
	framerate,
	flip_method);
 
    VideoCapture cap(pipeline, CAP_GSTREAMER);

    if(!cap.isOpened()) {
	cout << "Failed to open camera." << endl;
	return (-1);
    }
 
    while(true) {
    	if (!cap.read(img)) {
		cout << "Capture read error" << endl;
		break;
	}
	
	imshow("CSI Camera",img);

	int keycode = waitKey(10) & 0xff ; 
        if (keycode == 27) break ;
    }

    cap.release();
    destroyAllWindows() ;
    return 0;
}
