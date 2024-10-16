import cv2
import os
import concurrent.futures
import numpy as np
from rootsift import RootSIFT
from heapq import nsmallest
from time import sleep

rs = RootSIFT()

def extract_rootSIFT_features(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found or unable to load at path: {image_path}")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect keypoints and compute RootSIFT descriptors without Gabor filter
    detector = cv2.SIFT_create()
    kps = detector.detect(gray)

    # Draw keypoints
    keypoint_image = cv2.drawKeypoints(gray, kps, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the image with keypoints (window name based on image path to avoid conflicts)
    window_name = f"Keypoints - {os.path.basename(image_path)}"
    cv2.imshow(window_name, keypoint_image)
    
    # Keep the window open but continue the execution of the code
    cv2.waitKey(1)  # Short wait to refresh and move on

    (kps, descs) = rs.compute(gray, kps)

    # Debugging output
    if descs is None or len(descs) == 0:
        print(f"No descriptors found for image: {image_path}. Number of keypoints: {len(kps)}")

    return (kps, descs)

def match_image(image_path, descs_input):
    try:
        (kps_dataset, descs_dataset) = extract_rootSIFT_features(image_path)

        # Check if descriptors are valid
        if descs_input is None or descs_dataset is None:
            return (image_path, float('inf'))  # Avoid matching if any descriptor is None

        bf = cv2.BFMatcher()
        matches = bf.match(descs_input, descs_dataset)
        
        if len(matches) == 0:
            return (image_path, float('inf'))  # No matches found

        match_score = sum([m.distance for m in matches])

        return (image_path, match_score)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return (image_path, float('inf'))

def get_matches(input_image_path, dataset_directory):
    print(f"Processing input image: {input_image_path}")

    (kps_input, descs_input) = extract_rootSIFT_features(input_image_path)

    dataset_images = [os.path.join(dataset_directory, img) for img in os.listdir(dataset_directory)]
    print(f"Found {len(dataset_images)} images in dataset directory: {dataset_directory}")

    matches = []
    
    # Process images one by one and display them as they are processed
    for img_path in dataset_images:
        result = match_image(img_path, descs_input)
        if result[1] != float('inf'):  # Valid matches only
            matches.append(result)
    
    # Return top 26 matches
    return nsmallest(26, matches, key=lambda x: x[1])

input_image = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\to be matched\vinger01.jpg"  # Path to the input image
dataset_directory = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\image dataset"  # Path to the dataset

top_matches = get_matches(input_image, dataset_directory)

# Print the results while windows remain open
print("Matches ranked:")
for i, (image_path, score) in enumerate(top_matches):
    image_name = os.path.basename(image_path)
    print(f"{i+1}. {image_name}, score: {score}")

# Keep refreshing the windows so they stay open while printing results
while True:
    # Non-blocking wait to keep images open indefinitely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Close windows if 'q' is pressed

sleep(10 * 60)

# Ensure all windows are closed when done
cv2.destroyAllWindows()