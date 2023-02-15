from PIL import Image

# Load the original and current images
original_image = Image.open("original_image.jpg")
current_image = Image.open("current_image.jpg")

# Convert the images to RGB format
original_image = original_image.convert("RGB")
current_image = current_image.convert("RGB")

# Get the size of the images
width, height = original_image.size

# Set a threshold for color difference
threshold = 30

# Check if the color values of each pixel differ by more than the threshold
for x in range(width):
    for y in range(height):
        original_pixel = original_image.getpixel((x, y))
        current_pixel = current_image.getpixel((x, y))
        r_diff = abs(original_pixel[0] - current_pixel[0])
        g_diff = abs(original_pixel[1] - current_pixel[1])
        b_diff = abs(original_pixel[2] - current_pixel[2])
        if r_diff > threshold or g_diff > threshold or b_diff > threshold:
            print("Significant color difference detected!")
            break
    else:
        continue
    break
else:
    print("No significant color difference detected.")
