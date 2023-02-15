import cv2
import numpy as np

# Load the original and current images
original_image = cv2.imread(r'C:\Users\M_Thiruveedula\Downloads\Code Tester\decal\red_decal_flame.jpg')
#current_image = cv2.imread(r'C:\Users\M_Thiruveedula\Downloads\Code Tester\decal\image_red_faded2.jpg')
current_image = cv2.imread(r'C:\Users\M_Thiruveedula\Downloads\Code Tester\decal\image_red_faded1.jpeg')
#print("Original image shape: ", original_image.shape)
#print("Current image shape: ", current_image.shape)

# Resize the images to the same dimensions
#original_image = cv2.resize(original_image, current_image.shape[:2])
#print(original_image.shape)

# Resize the images to the same dimensions
#original_image = cv2.resize(original_image, current_image.shape[:2])

# Set a threshold for color difference
threshold = 30

# Calculate the absolute difference between the images
difference = cv2.absdiff(original_image, current_image)
"""
# Split the difference image into separate color channels
b, g, r = cv2.split(difference)

# Check if any pixel in any channel has a value greater than the threshold
if cv2.countNonZero(b > threshold) or cv2.countNonZero(g > threshold) or cv2.countNonZero(r > threshold):
    print("Significant color difference detected!")
else:
    print("No significant color difference detected.")

cv2.imshow('Original', original_image)
cv2.waitKey(0)
cv2.imshow('Faded', current_image)
cv2.waitKey(0)
"""
# Split the difference image into separate color channels
b, g, r = cv2.split(difference)

# Check if any pixel in any channel has a value greater than the threshold
if cv2.countNonZero(np.array(b > threshold, dtype=np.uint8)) or cv2.countNonZero(np.array(g > threshold, dtype=np.uint8)) or cv2.countNonZero(np.array(r > threshold, dtype=np.uint8)):
    print("Significant color difference detected!")
else:
    print("No significant color difference detected.")


