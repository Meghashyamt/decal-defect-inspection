import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert to Lab color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split into channels
l, a, b = cv2.split(lab)

# Calculate mean and standard deviation of a* and b* channels
a_mean, a_std = cv2.meanStdDev(a)
b_mean, b_std = cv2.meanStdDev(b)

# Threshold the standard deviation values
a_threshold = a_std[0][0] * 2
b_threshold = b_std[0][0] * 2

a_mask = cv2.threshold(a, a_threshold, 255, cv2.THRESH_BINARY)[1]
b_mask = cv2.threshold(b, b_threshold, 255, cv2.THRESH_BINARY)[1]

# Combine the masks
mask = cv2.bitwise_or(a_mask, b_mask)

# Apply morphological operations
kernel = np.ones((3,3), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=2)
mask = cv2.erode(mask, kernel, iterations=1)

# Find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over contours and find color fades
for c in contours:
    area = cv2.contourArea(c)
    if area > 1000:
        # Draw the contour on the image
        cv2.drawContours(img, [c], -1, (0,0,255), 2)

# Display the image
cv2.imshow('Color Fades', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
