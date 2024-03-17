import os
from PIL import Image

def process_images(input_folder, output_folder):
    """Converts images in the input folder to grayscale and saves them to the output folder."""
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (png or jpg)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            with Image.open(input_path) as img:
                # Convert the image to grayscale
                grayscale_img = img.convert('L')
                
                # Create a new image by copying pixel values from the grayscale image
                modified_img = grayscale_img.copy()
                
                # Get the dimensions of the image
                width, height = modified_img.size
                
                # Iterate over all pixels
                for y in range(height):
                    for x in range(width):
                        # Get the pixel value
                        pixel = grayscale_img.getpixel((x, y))
                        
                        # Check if the pixel is within the range of pure white (first 50 rows)
                        if y < 150:
                            if pixel >= 195:  # Change this threshold value to adjust the range
                                # Change pixels within the range to black
                                modified_img.putpixel((x, y), 0)
                            else:
                                # Change any other pixel to white
                                modified_img.putpixel((x, y), 255)
                        # Check if the pixel is within the range from white to gray (remaining rows)
                        else:
                            if pixel >= 165:  # Change this threshold value to adjust the range
                                # Change pixels within the range to black
                                modified_img.putpixel((x, y), 0)
                            else:
                                # Change any other pixel to white
                                modified_img.putpixel((x, y), 255)
                
                # Additional filling: Fill the area from (0, 0) to (20, 20) with white color
                for y in range(75):
                    for x in range(75):
                        modified_img.putpixel((x, y), 255)
                
                # Save the modified image
                modified_img.save(output_path)

input_folder = "./ws_photos/"
output_folder = "./final_photos/"
process_images(input_folder, output_folder)
