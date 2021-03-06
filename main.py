# pylint: disable=missing-module-docstring
import os
import re
import requests
​
try:
    import pytesseract as pyt
    from PIL import Image as img
    from bs4 import BeautifulSoup
    from pdf2image import convert_from_path
except ImportError:
    pass
​
​
class DataExtractor:
    """This class is used to extract text from the pdf and url files.
    """
​
    def __init__(self, question_type: str):
        """This function initializes the Extractor class.
​
        Args:
            question_type (str): _description_
        """
        self.question_type = question_type
        self.processed_text = ""
​
​
    def extract_pdf_data(self, pdf_path: str) -> str:
        """This function extracts the text from the pdf file.
​
        Args:
            pdf_path (str): The absolute path of the pdf file
​
        Returns:
            str: The processed text of the pdf file.
        """
        pages = convert_from_path(pdf_path, 0)
        for img_counter, page in enumerate(pages):
            # Extract pdf name to append to each page (image) name.
            file = os.path.split(pdf_path)[1]
            pdf_name = file.split('.')[0]
            file_name = f"{pdf_name}_page_{img_counter + 1}.jpg"
​
            # Save each page in image format.
            page.save(file_name, 'JPEG')
​
            # Extract raw text from the images and write to a output text file after processing.
            with open('pdf_output.txt', 'a') as outfile:
                extracted_raw_text = pyt.image_to_string(img.open(file_name))
                self.processed_text = extracted_raw_text.replace('-\n', '')
                outfile.write(self.processed_text)
        return self.processed_text
​
​
    
