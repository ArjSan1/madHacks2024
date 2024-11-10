import cv2
import pytesseract
from PIL import Image

def preprocess_and_ocr(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    
    # Use Tesseract for OCR
    pil_image = Image.fromarray(thresh)
    text = pytesseract.image_to_string(pil_image)
    
    print("Extracted Text:")
    print(text)
    return text

# Example usage
preprocess_and_ocr("image.png")
