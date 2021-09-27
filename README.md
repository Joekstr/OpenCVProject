# OpenCVProject
A game of Where's Waldo, run by OpenCV!

How to run program:
Type "python3 wheres_waldo.py -i puzzle.jpeg -r waldo.png -a help.png" into terminal.

Let's play Where's Waldo!
1. Load a Where's Waldo image.
2. Load a picture of Waldo.
3. Track wherever the user clicked.
4. Draw a mask over the image, showing only an area around where the player clicked.
5. Use OpenCV to see if Waldo is within the area that the user clicked.
  a. If not, allow them to retry.
  b. If so, highlight Waldo and congratulate the player!

Uses of each chapter:
Ch. 3: Loading the puzzle, waldo, and help images.
Ch. 4: Getting mouse coordinates in the click_and_mask function.
Ch. 5: Drawing a neon green rectangle around waldo when you find him.
Ch. 6: Creating a mask wherever you click.
Ch. 7: Creating an equalized version of the puzzle to make Waldo more obvious in the help section
Ch. 8: Using GaussianBlur to help draw contours around Waldo for the help section.
Ch. 9: Using a threshold to isolate Waldo from the background for the help section.
Ch. 10: Using Canny to draw contours around the edges of Waldo for the help section
Ch. 11: Drawing a neon green outline around Waldo for the help section.
