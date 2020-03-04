import numpy as np
import cv2
import matplotlib.pylab as plt

#%%----------------------------------------------------------------------------
#BINARZATION
dirpath = '..\\screenshots\\'
image = cv2.imread(dirpath + 'quad_3_lilcrop.png')
# image = cv2.resize(image, (1024, 576))
output = image.copy()
cvt_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#%%----------------------------------------------------------------------------
#HOUGH TRANSFORM
# circles = cv2.HoughCircles(cvt_image, cv2.HOUGH_GRADIENT, dp = 0.5,minDist= 5, param2=40, maxRadius = 50)
circles = cv2.HoughCircles(cvt_image, cv2.HOUGH_GRADIENT, dp = 5, minDist= 50, param2=300, minRadius = 70, maxRadius = 100)

if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 2)
		cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 128, 255), -1)
	# show the output image
	cv2.imwrite(dirpath + 'output.png', np.hstack([image, output]))
	cv2.waitKey(0)
else: print("no cricles found")
circles
