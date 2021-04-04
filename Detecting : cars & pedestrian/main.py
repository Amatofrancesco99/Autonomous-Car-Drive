########################################################################################################################
# @author: Amato Francesco
########################################################################################################################

# SOME USEFUL INFORMATION:

# OPENCV is an opensource computer-vision library, provided by some people who write some useful code (for example
# pre-trained classifiers, in this case we are going to use some pre-trained classifiers on "full-body" & "cars")

# To download opencv see this link: https://pypi.org/project/opencv-python/

# You have also to download, in the same folder of this script, other two files, which contains the pre-trained
# classifiers that I mentioned before (.xml file).
# You can find what I am saying at this link (read the copyright section before downloading & using it) :
#      https://github.com/opencv/opencv/tree/master/data/haarcascades/haarcascade_fullbody.xml
#      https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6   (haarcascade_cars.xml)

# You can find many other Haar Cascade Classifiers at this link... check if you're interested:
#      https://github.com/opencv/opencv/tree/master/data/haarcascades

########################################################################################################################
# SCRIPT:

# START
import cv2

# Pre-trained cars and pedestrians classifiers (Haar Cascade Classifier)
carTracker = cv2.CascadeClassifier('haarcascade_cars.xml')
pedestrianTracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Open a video which contains both cars & pedestrians in live-capture, like a car is "seeing"
# The downloaded video could be: https://www.youtube.com/watch?v=r90A4nv7vfI  (I've renamed it as:'demonstration_video')
# I suggest downloading not a 4K video resolution, but a less video resolution (1080 P) in order to make this sw just
# more fluent (let’s not let our CPU do unnecessary work extra...let’s treat "her" as best as we can  :')   )
video_capture = cv2.VideoCapture('demonstration_video.mp4')

# Iterate cars & pedestrians detection for every frame captured by our video stream
# (until we quit the app or the video ends)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # We must have to convert our frame to grayscale, because of how Haar Cascade works
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars and pedestrians (apply haar cascade algorithm to our img, to see how many cars or pedestrians are
    # present)
    # Those are the coordinates of all the cars that have been found
    cars = carTracker.detectMultiScale(gray)
    # Those are the coordinates of all the pedestrians that have been found
    pedestrians = pedestrianTracker.detectMultiScale(gray)

    # Now we want to put a rectangle around each car (in red), and each pedestrian (in yellow)
    # ... change color attributes if you're interested on different rectangles colour
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 1)

    # Show the result of the detection
    cv2.imshow('Detecting cars & pedestrians', frame)

    # Wait that the "q button" on the keyboard is been pressed, to then close the detecting app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()
        break  # END
# This application can be extended by adding some other features, for example to see (with another tele-camera that
# register the driver) if the driver is looking tired, if he closes his eyes, or where he is watching
# (all with eye-tracking).
# Maybe this sw could be expanded to control the distance between cars and regulate the speed (to avoid any accident)
# & so on...
