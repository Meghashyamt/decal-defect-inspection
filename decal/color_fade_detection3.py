import cv2
import numpy as np

# Load the original and faded images
original_image = cv2.imread("original_image.jpg")
faded_image = cv2.imread("faded_image.jpg")

# Convert the images to LAB color space
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)
faded_image = cv2.cvtColor(faded_image, cv2.COLOR_BGR2LAB)

# Split the images into separate channels
original_l, original_a, original_b = cv2.split(original_image)
faded_l, faded_a, faded_b = cv2.split(faded_image)

# Calculate the mean and standard deviation of the L channel in both images
original_l_mean, original_l_stddev = cv2.meanStdDev(original_l)
faded_l_mean, faded_l_stddev = cv2.meanStdDev(faded_l)

# Calculate the absolute difference between the mean L values
l_mean_diff = abs(original_l_mean - faded_l_mean)

# Calculate the sum of the standard deviations of the L channels
l_stddev_sum = original_l_stddev + faded_l_stddev

# Normalize the difference by the sum of the standard deviations
l_diff_norm = np.divide(l_mean_diff, l_stddev_sum)

# Set a threshold for the normalized difference
threshold = 0.1

# Check if the normalized difference is greater than the threshold
if l_diff_norm > threshold:
    print("The image has faded compared to the original.")
else:
    print("The image has not faded compared to the original.")
