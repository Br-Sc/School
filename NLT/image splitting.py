from PIL import Image
import concurrent.futures

# Function to find near-black line positions (RGB between 0,0,0 and 25,25,25)
def find_black_lines(image):
    width, height = image.size
    black_lines = []

    # Define the maximum RGB value for the near-black lines (inclusive)
    tolerance = (25, 25, 25)

    # Loop through each column (x-coordinate)
    for x in range(width):
        is_black_line = True

        # Check if the entire column is within the tolerance for near-black
        for y in range(height):
            pixel = image.getpixel((x, y))
            if not (0 <= pixel[0] <= tolerance[0] and 0 <= pixel[1] <= tolerance[1] and 0 <= pixel[2] <= tolerance[2]):
                is_black_line = False
                break
        
        # If it's a near-black line, store its x position
        if is_black_line:
            black_lines.append(x)

    return black_lines

# Function to process and split an image based on black or near-black lines
def process_image(img_path):
    try:
        # Open the image
        image = Image.open(img_path)

        # Find black or near-black line positions
        black_lines = find_black_lines(image)

        # Check if there are at least 4 black lines
        if len(black_lines) < 4:
            raise ValueError("Less than 4 black lines detected in the image")

        # Split image based on black lines
        split_positions = [0] + black_lines + [image.size[0]]  # Include 0 and image width

        for i in range(len(black_lines)):
            left = split_positions[i] + 1  # Left side of the split (add 1 to avoid the black line)
            right = split_positions[i + 1]  # Right side of the split
            cropped_img = image.crop((left, 0, right, image.size[1]))

            # Save each cropped section
            cropped_img.save(f"output_part_{i+1}_{img_path.split('\\')[-1]}")

        print(f"Processed: {img_path}")

    except Exception as e:
        print(f"Error processing {img_path}: {e}")

# Use ThreadPoolExecutor to process images in parallel
def process_images_in_parallel(image_paths):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, image_paths)

# List of image file paths
image_paths = [
    r"C:\Users\galax\Desktop\temp\lars sanders links.jpg",
    r"C:\Users\galax\Desktop\temp\lars sanders rechts.jpg",
    r"C:\Users\galax\Desktop\temp\maria johanna helder links.jpg",
    r"C:\Users\galax\Desktop\temp\maria johanna helder rechts.jpg",
    r"C:\Users\galax\Desktop\temp\merel elisabeth schooneveld links.jpg",
    r"C:\Users\galax\Desktop\temp\merel elisabeth schooneveld rechts.jpg",
    r"C:\Users\galax\Desktop\temp\rachel janssen links.jpg",
    r"C:\Users\galax\Desktop\temp\rachel janssen rechts.jpg",
    r"C:\Users\galax\Desktop\temp\rene gerardus nicolaas claasens links.jpg",
    r"C:\Users\galax\Desktop\temp\rene gerardus nicolaas claasens rechts.jpg",
    r"C:\Users\galax\Desktop\temp\robert vink links.jpg",
    r"C:\Users\galax\Desktop\temp\robert vink rechts.jpg",
    r"C:\Users\galax\Desktop\temp\roger de jager links.jpg",
    r"C:\Users\galax\Desktop\temp\roger de jager rechts.jpg",
    r"C:\Users\galax\Desktop\temp\tobar yoska links.jpg",
    r"C:\Users\galax\Desktop\temp\tobar yoska rechts.jpg",
    r"C:\Users\galax\Desktop\temp\egbert adrianus sanders links.jpg",
    r"C:\Users\galax\Desktop\temp\egbert adrianus sanders rechts.jpg",
    r"C:\Users\galax\Desktop\temp\hannah catharina hoogendoorn links.jpg",
    r"C:\Users\galax\Desktop\temp\hannah catharina hoogendoorn rechts.jpg",
    r"C:\Users\galax\Desktop\temp\huub cornelius henselmans links.jpg",
    r"C:\Users\galax\Desktop\temp\huub cornelius henselmans rechts.jpg",
    r"C:\Users\galax\Desktop\temp\jolien marit sanders van opdam links.jpg",
    r"C:\Users\galax\Desktop\temp\jolien marit sanders van opdam rechts.jpg",
    r"C:\Users\galax\Desktop\temp\katie anne schipper links.jpg",
    r"C:\Users\galax\Desktop\temp\katie anne schipper rechts.jpg"
]

# Execute the function to process images
if __name__ == "__main__":
    process_images_in_parallel(image_paths)
    print("All images processed.")
