# kps = keypoints
# descs = descriptors

import cv2
import os
import concurrent.futures

from rootsift import RootSIFT
from heapq import nsmallest
from time import sleep


rs = RootSIFT()


def extract_rootSIFT_features(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found or unable to load at path: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.SIFT_create()
    kps = detector.detect(gray)

    (kps, descs) = rs.compute(gray, kps)
    
    return (kps, descs)



def match_image(image_path, descs_input):
    try:
        (kps_dataset, descs_dataset) = extract_rootSIFT_features(image_path)
        
        bf = cv2.BFMatcher()
        matches = bf.match(descs_input, descs_dataset)
        match_score = sum([m.distance for m in matches])
        
        if descs_dataset is None:
            return (image_path, float('inf'))
        
        return (image_path, match_score)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return (image_path, float('inf'))



def get_matches(input_image_path, dataset_directory):
    print(f"Processing input image: {input_image_path}")
    
    (kps_input, descs_input) = extract_rootSIFT_features(input_image_path)
    
    dataset_images = [os.path.join(dataset_directory, img) for img in os.listdir(dataset_directory)]
    print(f"Found {len(dataset_images)} images in dataset directory: {dataset_directory}")
    
    for img_path in dataset_images:
        print(f"Processing dataset image: {img_path}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(match_image, img_path, descs_input) for img_path in dataset_images]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    matches = nsmallest(130, results, key=lambda x: x[1])

    return matches


input_image = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\to be matched\vinger07.jpg" # Needs to include directory, for example "C:\Users\user\Pictures\picture.jpg".
dataset_directory = r"C:\Users\galax\Downloads\Coding\Python\Image comparing\image dataset split"


top_matches = get_matches(input_image, dataset_directory)

print("Matches ranked:")
for i, (image_path, score) in enumerate(top_matches):
    image_name = os.path.basename(image_path)
    print(f"{i+1}. {image_name}, score: {score}")

sleep(10 * 60)