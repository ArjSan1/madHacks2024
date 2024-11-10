import easyocr

# Function for EasyOCR
def ocr_with_easyocr(image_path):
    reader = easyocr.Reader(['en'], gpu=False)  # Use GPU if available
    try:
        results = reader.readtext(image_path, detail=0)
        return "\n".join(results)
    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except Exception as e:
        return f"Error during EasyOCR processing: {e}"

# Main OCR function
def perform_text_recognition(image_path):
    print("\nAttempting OCR with EasyOCR...")
    easyocr_result = ocr_with_easyocr(image_path)
    print("OCR Output:")
    print(easyocr_result)
    return easyocr_result  # Return the result to be used in other files
