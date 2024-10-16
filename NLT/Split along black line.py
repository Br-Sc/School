import cv2
from PIL import Image
import numpy as np
import os

# Function to find black vertical lines in the image
def find_black_lines(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image to make the black lines stand out
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # Sum the values in each column to find the vertical black lines
    vertical_sum = np.sum(thresh, axis=0)
    
    # Find where the sum is high, indicating black lines
    threshold_value = np.max(vertical_sum) * 0.8  # Adjust the sensitivity here if needed
    line_positions = np.where(vertical_sum > threshold_value)[0]
    
    # Return all detected line positions
    return line_positions

# Function to split the image based on the black lines
def split_image_by_black_lines(image_path, output_folder):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    
    # Find positions of the black lines
    black_lines = find_black_lines(image)
    
    # Create output directory if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the image using PIL for saving the split parts
    pil_image = Image.open(image_path)
    
    # Add the left and right boundaries to the list of lines for complete splitting
    black_lines = np.insert(black_lines, 0, 0)  # Add the left boundary (0)
    black_lines = np.append(black_lines, width)  # Add the right boundary (image width)
    
    # Split and save each section based on the black lines
    for i in range(len(black_lines) - 1):
        left = black_lines[i]
        right = black_lines[i + 1]
        split_img = pil_image.crop((left, 0, right, height))
        split_img.save(os.path.join(output_folder, f'{os.path.basename(image_path).split(".")[0]}_part_{i + 1}.png'))

# Function to process all images in a given folder
def process_images_in_folder(input_folder, output_folder):
    # Get list of all image files in the folder (jpg, png, etc.)
    supported_formats = ('.jpg', '.jpeg', '.png')
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_formats)]
    
    # Process each image file
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        print(f"Processing: {image_path}")
        split_image_by_black_lines(image_path, output_folder)

# Folder containing the images
input_folder = r'C:\Users\galax\Downloads\Coding\Python\Image comparing\image dataset'  # Specify the input folder

# Folder to save the split images
output_folder = r'C:\Users\galax\Downloads\Coding\Python\Image comparing\image dataset split'  # Specify output folder

# Process all images in the input folder
process_images_in_folder(input_folder, output_folder)

print("All images in the folder have been split and saved successfully.")
