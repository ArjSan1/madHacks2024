import re

def extract_id_info(ocr_text):
    """
    Extracts the date of birth, full name, and address from OCR-processed text of an ID.

    Parameters:
    ocr_text (str): The OCR-processed text from the ID.

    Returns:
    dict: A dictionary containing 'date_of_birth', 'full_name', and 'address'.
    """

    # Initialize the result dictionary
    result = {
        'date_of_birth': 'DOB not found',
        'first': 'Name not found',
        'last': 'Name not found',
        'address': 'Address not found'
    }

    dob_match = re.search(r"\bDOB[:\s]*([\d/]+)", ocr_text)
    dob = dob_match.group(1) if dob_match else "DOB not found"
    result['date_of_birth'] = dob

    # Extract Full Name
    name_match = re.search(r"([A-Z]+)\s*2\s*([A-Z]+)", ocr_text)
    last_name = name_match.group(1).strip() if name_match else "Last name not found"
    first_name = name_match.group(2).strip() if name_match else "First name not found"
    result['first'] = first_name
    result['last'] = last_name

    # Extract Address
    address_match = re.search(r"\d{2,5}.*?[A-Za-z\s].*?[A-Z]\s\d{5}", ocr_text)
    address = address_match.group(0).strip() if address_match else "Address not found"
    result['address'] = address.replace("\n", " ")

    return result