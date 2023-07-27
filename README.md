# Gender_detection
#Gender Detection in an Image using OpenCV and cvlib
This code demonstrates gender detection in an image using OpenCV and the cvlib library. The script reads an image file, detects faces in the image, and predicts the gender of each detected face.

#Requirements
Python 3.x
OpenCV
cvlib
NumPy

#Usage
Clone the repository or download the script directly.
Make sure to have an image file available.
Update the image_path variable in the script with the path to your image file.
Install the required dependencies by running the following command:
Copy code
pip install opencv-python cvlib numpy
Run the script using the following command:
Copy code
python gender_detection_image.py
A new window will open, displaying the original image with rectangles and gender annotations on each detected face.
Press any key to close the window and terminate the program.

#How It Works
The script reads an image file using OpenCV's imread() function.
Each face in the image is detected using the cv.detect_face() function from the cvlib library.
For each detected face, a rectangle is drawn around it.
The face region is cropped from the image and passed to the cv.detect_gender() function from cvlib to predict the gender.
The gender label and confidence percentage are displayed on the image.
The annotated image is shown in a new window.
Pressing any key closes the window and terminates the program.
