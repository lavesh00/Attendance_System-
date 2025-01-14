import os
import face_recognition
import pickle
from tqdm import tqdm  # For progress bar

# Path to known student images
known_faces_dir = "C:\\Users\\asus\\Downloads\\AI\\attendance_system\\student_images"
encodings_file = "C:\\Users\\asus\\Downloads\\AI\\attendance_system\\encodings.pkl"

# Dictionary to store encodings and their corresponding IDs
face_encodings = {}

# Track processing with a progress bar
image_files = [f for f in os.listdir(known_faces_dir) if f.endswith(('.JPG', '.jpeg', '.png'))]
print(f"Found {len(image_files)} images to process.")

for filename in tqdm(image_files, desc="Processing images"):
    try:
        student_id = os.path.splitext(filename)[0]  # Extract student ID from filename
        image_path = os.path.join(known_faces_dir, filename)

        # Load and encode the image
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        
        if encodings:
            # If a student already has encodings, add to the list; otherwise, create a new list
            if student_id not in face_encodings:
                face_encodings[student_id] = []
            face_encodings[student_id].append(encodings[0])  # Store all encodings for the student
        else:
            print(f"Warning: No face detected in {filename}. Skipping.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Compute average encoding for students with multiple images
average_encodings = {student_id: sum(encodings) / len(encodings) for student_id, encodings in face_encodings.items()}

# Save encodings to a file
with open(encodings_file, 'wb') as f:
    pickle.dump(average_encodings, f)

print("Face encodings saved successfully!")
