from regex_module import extract_id_info
from ocr_module import perform_text_recognition

id_file_path = input("Please provide the path to your ID file: ").strip()
ocr_text = perform_text_recognition(id_file_path)
extracted_info = extract_id_info(ocr_text)

print(extracted_info)