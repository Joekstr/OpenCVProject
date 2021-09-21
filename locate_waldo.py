#import packages 👍
import argparse
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt
from apply_mask import clicker

#parse two arguments: a picture of the puzzle itself, and a reference picture of waldo
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "puzzle pic")
ap.add_argument("-r", '--reference', required = True, help = "waldo ref pic")
args = vars(ap.parse_args())

#saves the pictures, then grayscales them so that opencv can identify waldo easier
puzzle = cv2.imread(args['image'])
puzzle_gray = cv2.cvtColor(puzzle, cv2.COLOR_BGR2GRAY)
reference = cv2.imread(args['reference'])
reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
# saves the height and width of the reference picture into 'h' and 'w'
h, w = reference_gray.shape[::]

#cross referencing the reference pic of waldo to the puzzle to find waldo
res = cv2.matchTemplate(puzzle_gray,reference_gray,cv2.TM_CCOEFF_NORMED)
#change how sensitive the matching is
threshold = 0.4

# finding the values where it exceeds the threshold
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    #draw rectangle on places where it exceeds threshold
    cv2.rectangle(puzzle, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

cv2.imshow('GOTTEM',puzzle)
cv2.waitKey(0)
