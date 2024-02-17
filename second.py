import os
import pytesseract
from PIL import Image

def extract_text_from_images(input_folder, output_file):
    """
    Extracts text from all images in the folder and writes it to a single txt file.
    
    :param input_folder: Path to the folder containing images.
    :param output_file: Path to the file where the text will be written.
    """
    # Open the file for writing
    with open(output_file, 'w', encoding='utf-8') as f:
        # Iterate over all files in the input folder
        for filename in os.listdir(input_folder):
            # Check if the file is an image (png, jpg, or jpeg)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(input_folder, filename)
                
                # Open the image
                with Image.open(image_path) as img:
                    # Use Tesseract to extract text from the image
                    text = pytesseract.image_to_string(img)
                    
                    # Write the text to the file
                    f.write(text + '\n')  # Add a newline character between texts

# Paths to the input folder and the output file
input_folder = "./final_photos/"
output_file = "output.txt"

# Call the function to extract text from images and write it to the output file
extract_text_from_images(input_folder, output_file)
