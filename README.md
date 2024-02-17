# Image Text Extractor

This application is designed to extract text from images using Tesseract OCR. It supports processing images in PNG, JPG, and JPEG formats.

## Installation

1. Install the necessary dependencies by running the following command:

    ```
    pip install pillow pytesseract
    ```

2. Make sure you have Tesseract OCR installed. Installation instructions can be found on the [official Tesseract website](https://github.com/tesseract-ocr/tesseract).

3. Clone the repository using the following command:

    ```
    git clone https://github.com/your_username/image-text-extractor.git
    ```

## Usage

1. Place the images from which you want to extract text into the `input_images` folder.

2. Run the `main.py` and `second.py` script to extract text from the images:

    ```
    python3 main.py
    python3 second.py
    ```

3. The extracted text will be saved in the `output.txt` file.

## Notes

- Ensure that the images are of good quality and the text on them is legible for better text extraction results.

- If necessary, you can adjust the Tesseract OCR parameters in the `second.py` file to improve text extraction results.
