#import packages 👍
import argparse
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt

def locate(image, reference):
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
    if len(loc[::-1][0]) > 1:
        found = True
        cv2.imshow('GOTTEM',puzzle)
        cv2.waitKey(0)
    return found
