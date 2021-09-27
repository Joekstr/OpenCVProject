#import packages 👍
import argparse
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt

#function takes in a masked puzzle and reference picture of waldo and checks if waldo is within the masked area of the puzzle
def locate(image, reference):
    #a boolean to detect if waldo is found
    found = False
    #saves the pictures, then grayscales them so that opencv can identify waldo easier
    puzzle = image
    puzzle_gray = cv2.cvtColor(puzzle, cv2.COLOR_BGR2GRAY)
    reference = reference
    reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    # saves the height and width of the reference picture into 'h' and 'w'
    h, w = reference_gray.shape[::]

    #cross referencing the reference pic of waldo to the puzzle to find waldo
    res = cv2.matchTemplate(puzzle_gray,reference_gray,cv2.TM_CCOEFF_NORMED)
    #change how sensitive the matching is
    threshold = 0.45

    # finding the values where it exceeds the threshold
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(puzzle, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    #if it detects a waldo in the area you clicked, set found to true
    if len(loc[::-1][0]) > 1:
        found = True
        cv2.imshow('YOU FOUND WALDO!', puzzle)
        cv2.waitKey(0)

    #return whether waldo was found
    return found
