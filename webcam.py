import cv2

def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Unable to open the webcam.")
        return

    # Read the image from the webcam
    ret, frame = cap.read()

    # Check if the image was successfully captured
    if not ret:
        print("Failed to capture the image.")
        return

    # Release the webcam
    cap.release()
    save_directory = "D:\machine learning"

    # Save the captured image to the specified directory
    image_path = f"{save_directory}/captured_image.jpg"
    cv2.imwrite(image_path, frame)

    print(f"Image saved successfully: {image_path}")
    return image_path

# Set the directory where the image will be saved


# Call the capture_image function

