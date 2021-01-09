// OpenCVTest.cpp : This file contains the 'main' function. 
// Program execution begins and ends there.


#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
	Mat image = Mat::zeros(300, 600, CV_8UC3);
	circle(image, Point(250, 150), 100, Scalar(100, 140, 120), -100);
	circle(image, Point(390, 150), 100, Scalar(0, 0, 230), -100);
	circle(image, Point(320, 180), 100, Scalar(120, 255, 255), -100);
	imshow("Display Window", image);
	waitKey(0);
	return 0;
}

