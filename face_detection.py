import cv2
import time

# Load the trained cascade classifiers for close and far distance face detection
far_cascade = cv2.CascadeClassifier(r'C:\Users\USER\Desktop\final_face_detect\classifier\cascade_version1.xml')
# far_cascade = cv2.CascadeClassifier(r'C:\Users\USER\Desktop\cascade_version2.xml')

# Open a connection to the camera (0 is typically the built-in webcam, but you can change it to the appropriate camera index)
cap = cv2.VideoCapture(0)

min_face_size = (10, 10)  # Starting minimum size
max_face_size = (200, 200)  # Starting maximum size

total_time_per_image = 0
total_face_detection_time = 0
total_faces_detected = 0
num_frames = 0

while True:
    num_frames += 1

    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame for far distance
    start_time = time.time()
    far_faces = far_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=3, minSize=(120, 120))
    end_time = time.time()
    elapsed_time = end_time - start_time

    total_time_per_image += elapsed_time

    # Count the number of faces detected in the current frame
    num_faces_detected = len(far_faces)
    total_faces_detected += num_faces_detected

    # Sum the face detection time for this frame
    total_face_detection_time += elapsed_time

    # Draw rectangles around detected far-distance faces
    for (x, y, w, h) in far_faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Update minimum and maximum face sizes
    if num_frames == 30:
        print("Minimum detectable face size:", min_face_size)
        print("Maximum detectable face size:", max_face_size)
        min_face_size = (min_face_size[0] + 10, min_face_size[1] + 10)
        max_face_size = (max_face_size[0] - 10, max_face_size[1] - 10)
        num_frames = 0

# Calculate averages
average_time_per_image = total_time_per_image / num_frames
average_time_per_face = total_face_detection_time / total_faces_detected

print("Average detection time per image:", average_time_per_image)
print("Average detection time per face:", average_time_per_face)

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
