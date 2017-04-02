import numpy as np
import cv2

def main_func():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # #grayscale image to binary
        # im_bw = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY)[1]

        # Display the resulting frame
        cv2.imshow('frame',im_gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main_func()