import argparse
import cv2
import numpy as np
from locate_waldo import locate

#parse two arguments: a picture of the puzzle itself, and a reference picture of waldo
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-r", '--reference', required = True, help = "waldo ref pic")
ap.add_argument("-a", '--assist', required = True, help = "pic of waldo to edit into helpful location images")

args = vars(ap.parse_args())
ref = cv2.imread(args["reference"])
help = cv2.imread(args["assist"])

#a function that detects mouse inputs and creates a mask around a clicked region.
def click_and_mask(event,x,y,flags,parameters):
    #import the reference image into the function
    global ref
    #check if the mouse was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        #create a circle mask on the puzzle
        mask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.circle(mask,(x,y),150,255,-1)
        masked = cv2.bitwise_and(image,image,mask = mask)
        #check if waldo was found
        locate(masked, ref)
        if locate(masked, ref) == False:
            cv2.imshow("YOU DIDN'T FIND WALDO! PRESS R TO RETRY",masked)


# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)")
cv2.setMouseCallback("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)", click_and_mask)

#similar to an Update() function that's called once per frame; keep running this until it detects a mouse click, then run click_and_mask()
while True:
    #show puzzle
    cv2.imshow("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)",image)
    key = cv2.waitKey(1) & 0xFF
    #retry protocol
    if key == ord("r"):
        cv2.destroyAllWindows()
        cv2.imshow("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)",image)
        cv2.setMouseCallback("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)", click_and_mask)
        key = cv2.waitKey(1) & 0xFF
    #quit game
    if key == ord("q"):
        break
    #help menu
    if key == ord("h"):
        cv2.destroyAllWindows()
        #set up all the different pictures for help
        gray = cv2.cvtColor(help, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5,5), 0)
        edgy = cv2.Canny(blurred,30,500)
        (cnts, _) = cv2.findContours(edgy.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        waldoes = help.copy()
        cv2.drawContours(waldoes,cnts,-1,(0,255,0),2)
        (T,thresh) = cv2.threshold(blurred,195,255,cv2.THRESH_BINARY_INV)
        gray_puzzle = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eq = cv2.equalizeHist(gray_puzzle)
        #show equalized black and white picture
        cv2.imshow("An equalized black and white picture of the puzzle. Maybe something'll catch your eye?", np.hstack([gray_puzzle,eq]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #show a thresholded waldo
        cv2.imshow("Here he is without some of the distracting background.", cv2.bitwise_and(help,help,mask=thresh))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #show outlined waldo
        cv2.imshow("Here he is outlined in an obvious green outline!", waldoes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #reshow puzzle
        cv2.imshow("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)",image)
        cv2.setMouseCallback("WHERE'S WALDO? CLICK THE PART OF THE SCREEN WHERE YOU THINK HE IS! (PRESS H FOR HELP)", click_and_mask)
        key = cv2.waitKey(1) & 0xFF
