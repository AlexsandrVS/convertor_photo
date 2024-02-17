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
                
                # Iterate over all pixels and change colors according to requirements
                for x in range(width):
                    for y in range(height):
                        pixel = modified_img.getpixel((x, y))
                        if pixel < 128:
                            modified_img.putpixel((x, y), 255)  # Change black pixels to white
                        elif pixel > 128:
                            modified_img.putpixel((x, y), 0)    # Change white pixels to black
                        # Remove gray pixels
                        # Do nothing, they will remain transparent

                # Save the modified image
                modified_img.save(output_path)

input_folder = "./ws_photos/"
output_folder = "./final_photos/"
process_images(input_folder, output_folder)
