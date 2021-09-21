import argparse
import cv2
import numpy as np

def click_and_mask(event,x,y,flags,parameters):
        if event == cv2.EVENT_LBUTTONDOWN:
            mask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.circle(mask,(x,y),150,255,-1)
            masked = cv2.bitwise_and(image,image,mask = mask)
            cv2.imshow("YOU DIDN'T FIND WALDO! PRESS R TO RETRY",masked)
            masking = masked

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("WHERE'S WALDO?")
cv2.setMouseCallback("WHERE'S WALDO?", click_and_mask)

while True:
    cv2.imshow("WHERE'S WALDO?",image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        cv2.destroyAllWindows()
        cv2.imshow("WHERE'S WALDO?",image)
        cv2.setMouseCallback("WHERE'S WALDO?", click_and_mask)
        key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
