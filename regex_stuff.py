from ocr_module import perform_text_recognition
import re

# Path to the ID image
id_file_path = input("Please provide the path to your ID file: ").strip()

# Call the OCR function and store the result in a variable
ocr_text = perform_text_recognition(id_file_path)

# Use the OCR result as needed
print("\nOCR Result from ID image:")
print(ocr_text)

dob_match = re.search(r"\bDOB[:\s]*([\d/]+)", ocr_text)
dob = dob_match.group(1) if dob_match else "DOB not found"

# Extract Full Name
name_match = re.search(r"([A-Z]+)\s*2\s*([A-Z]+)", ocr_text)
last_name = name_match.group(1).strip() if name_match else "Last name not found"
first_name = name_match.group(2).strip() if name_match else "First name not found"

# Extract Address
address_match = re.search(r"\d{2,5}.*?[A-Za-z\s].*?[A-Z]\s\d{5}", ocr_text)
address = address_match.group(0).strip() if address_match else "Address not found"

print(f"Date of Birth: {dob}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Address: {address}")