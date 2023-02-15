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

# Apply morphological operations to remove noise and smooth the mask
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Apply the mask to the modified image to highlight the defects
defects = cv2.bitwise_and(modified, modified, mask=mask)

# Display the results
cv2.imshow('Original', original)
cv2.imshow('Modified', modified)
cv2.imshow('Defects', defects)
cv2.waitKey(0)
cv2.destroyAllWindows()
