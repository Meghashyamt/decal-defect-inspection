import cv2

# Load the original and modified images
original = cv2.imread(r'C:\Users\M_Thiruveedula\Downloads\Code Tester\decal\red_decal_flame.jpg')
modified = cv2.imread(r'C:\Users\M_Thiruveedula\Downloads\Code Tester\decal\image_defect2.png')

# Convert images to grayscale
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
modified_gray = cv2.cvtColor(modified, cv2.COLOR_BGR2GRAY)

# Compute the absolute difference between the two images
diff = cv2.absdiff(original_gray, modified_gray)

# Threshold the difference image to create a binary mask of the defects
threshold_value = 20
ret, mask = cv2.threshold(diff, threshold_value, 255, cv2.THRESH_BINARY)

# Find contours in the binary mask
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes on the modified image
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(modified, (x, y), (x+w, y+h), (0, 255, 0), 1)

# Display the results
cv2.imshow('Original', original)
cv2.imshow('Modified', modified)
cv2.waitKey(0)
cv2.destroyAllWindows()
