import os
from PIL import Image

def process_images(input_folder, output_folder):
    """Converts images in the input folder to grayscale and saves them to the output folder."""
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the color ranges with tolerance
    color_ranges = [
        ((43, 161, 215), (92, 220, 260)),   # Original blue range
        ((47, 147, 214), (68, 167, 234)),   # Additional blue range 1
        ((40, 145, 208), (61, 165, 228)),   # Additional blue range 2
        ((53, 146, 195), (74, 166, 215)),   # Additional blue range 3
        ((52, 180, 239), (73, 200, 259)),   # Additional blue range 4
        ((93, 213, 243), (114, 233, 263)),  # Additional blue range 5
        ((152, 120, 83), (174, 140, 103))   # New color range
    ]

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
                        r, g, b = img.getpixel((x, y))
                        
                        # Check if the pixel is within any of the color ranges
                        for min_vals, max_vals in color_ranges:
                            min_r, min_g, min_b = min_vals
                            max_r, max_g, max_b = max_vals
                            if (min_r <= r <= max_r) and (min_g <= g <= max_g) and (min_b <= b <= max_b):
                                modified_img.putpixel((x, y), 0)  # Change pixels in the range to black
                                break  # Exit the loop after finding the matching range
                            
                        # Change black and white pixels as before
                        pixel = modified_img.getpixel((x, y))
                        if pixel < 128:
                            modified_img.putpixel((x, y), 255)  # Change black pixels to white
                        elif pixel > 128:
                            modified_img.putpixel((x, y), 0)    # Change white pixels to black
                        # Remove gray pixels
                        # Do nothing, they will remain transparent

                # Save the modified image
                modified_img.save(output_path)

input_folder = "./ws/"
output_folder = "./fin/"
process_images(input_folder, output_folder)
