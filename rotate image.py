import cv2

# Load the original image
original_image = cv2.imread("C:\\Users\\deepika\\OneDrive - Kamaraj College of Engineering and Technology\\Pictures\\Saved Pictures\\mm.jpg")
  # Replace "your_image.jpg" with your image file path

# Check if the image was loaded successfully
if original_image is None:
    print("Error: Unable to load image.")
else:
    # Get the height and width of the image
    height, width = original_image.shape[:2]

    # Rotate the image 90 degrees clockwise
    rotated_image_90 = cv2.rotate(original_image, cv2.ROTATE_90_CLOCKWISE)

    # Rotate the image 180 degrees
    rotated_image_180 = cv2.rotate(original_image, cv2.ROTATE_180)

    # Rotate the image 270 degrees clockwise
    rotated_image_270 = cv2.rotate(original_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Save the rotated images
    cv2.imwrite("tester1.png", rotated_image_90)
    cv2.imwrite("tester2.png", rotated_image_180)
    cv2.imwrite("tester3.png", rotated_image_270)

    print("Images successfully rotated and saved as tester1.png, tester2.png, and tester3.png.")

# Display the original image
cv2.imshow("Original Image", original_image)
cv2.imshow("rotate 90",rotated_image_90)
cv2.imshow("rotate 180", rotated_image_180)
cv2.imshow("rotate 270",rotated_image_270)
cv2.waitKey(0)
cv2.destroyAllWindows()
