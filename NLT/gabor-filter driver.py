import cv2
import os
import concurrent.futures
import numpy as np
from rootsift import RootSIFT
from heapq import nsmallest
from time import sleep

rs = RootSIFT()

def gabor_filter(image):
    # Parameters for Gabor filter
    kernel_size = 21
    sigma = 5.0
    theta = np.pi / 4  # Angle in radians
    lambd = 10.0  # Wavelength of the cosine factor
    gamma = 0.5  # Spatial aspect ratio
    psi = 0  # Phase offset

    # Create Gabor kernel
    gabor_kernel = cv2.getGaborKernel((kernel_size, kernel_size), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_32F)
    filtered_image = cv2.filter2D(image, cv2.CV_8UC3, gabor_kernel)

    return filtered_image

def extract_rootSIFT_features(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found or unable to load at path: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gabor filter
    filtered_image = gabor_filter(gray)

    # Detect keypoints and compute RootSIFT descriptors
    detector = cv2.SIFT_create()
    kps = detector.detect(filtered_image)

    (kps, descs) = rs.compute(filtered_image, kps)

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

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(match_image, img_path, descs_input) for img_path in dataset_images]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    # Filter out results with infinite scores
    results = [result for result in results if result[1] != float('inf')]
    
    matches = nsmallest(26, results, key=lambda x: x[1])

    return matches

input_image = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\to be matched\vinger07.jpg"  # Path to the input image
dataset_directory = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\image dataset"  # Path to the dataset

top_matches = get_matches(input_image, dataset_directory)

print("Matches ranked:")
for i, (image_path, score) in enumerate(top_matches):
    image_name = os.path.basename(image_path)
    print(f"{i+1}. {image_name}, score: {score}")

sleep(10 * 60)
