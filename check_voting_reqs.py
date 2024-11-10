import pandas as pd
import os
from PIL import Image
import cv2
import easyocr

# Load the CSV file with voting requirements
csv_path = 'absentee_voting_requirements.csv'
df = pd.read_csv(csv_path)

# Convert DataFrame to dictionary for easy lookup by state
requirements = df.set_index('State').to_dict(orient='index')


# Function for EasyOCR
def ocr_with_easyocr(image_path):
    reader = easyocr.Reader(['en'], gpu=False)  # Use GPU if available
    results = reader.readtext(image_path, detail=0)
    
    print("EasyOCR Output:")
    print("\n".join(results))
    return "\n".join(results)



# Main OCR function to test multiple models
def perform_text_recognition(image_path, model_path=None):
    
    print("\nAttempting OCR with EasyOCR...")
    easyocr_result = ocr_with_easyocr(image_path)


    # Return the results from all methods
    return {
        "EasyOCR": easyocr_result,
    }

# Main function to check requirements
def check_state_requirements(state):
    state_info = requirements.get(state)
    if not state_info:
        print(f"No information available for {state}.")
        return
    
    excuse_required = state_info['Excuse Required'].strip().lower() == 'yes'
    id_required = not state_info['ID or Other Requirements'].strip().lower().startswith("no id")

    print(f"\nState: {state}")
    print(f"Excuse Required: {'Yes' if excuse_required else 'No'}")
    print(f"ID Required: {'Yes' if id_required else 'No'}")
    
    if excuse_required:
        print("\nAcceptable Excuses:")
        excuses = state_info['Acceptable Excuses'].split(';')
        for i, excuse in enumerate(excuses, 1):
            print(f"{i}. {excuse.strip()}")
        selected_excuse = input("\nSelect an excuse by number: ").strip()
        try:
            selected_excuse = int(selected_excuse)
            if 1 <= selected_excuse <= len(excuses):
                print(f"You selected: {excuses[selected_excuse - 1].strip()}")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if id_required:
        print("\nAn ID is required for absentee voting in this state.")
        id_file_path = input("Please provide the path to your ID file: ")
        
        # Perform OCR on the uploaded ID file using multiple methods
        print("\nPerforming OCR on the ID with multiple methods...")
        ocr_results = perform_text_recognition(id_file_path)
        for method, result in ocr_results.items():
            print(f"\n{method} OCR Result:")
            print(result)
    else:
        print("\nNo ID is required for absentee voting in this state.")

if __name__ == "__main__":
    state = input("Enter the state to check absentee voting requirements: ").strip()
    check_state_requirements(state)
