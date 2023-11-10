import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# Open the PDF document
pdf_document = fitz.open("sample.pdf")

# Initialize the final text container
extracted_text = ""

for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    
    # Render the page as an image
    pix = page.get_pixmap(alpha=False)
    
    # Convert the image data to a format that Tesseract can work with (e.g., PIL Image)
    image_data = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    print(image_data)
    
    # Perform OCR to extract text from the image
    text = pytesseract.image_to_string(image_data, lang='eng', config=r'--psm 3 --oem 1')
    
    # Append the extracted text to the result
    extracted_text += text + "\n"

print(extracted_text)
# Replace this with the path to your output text file
output_text_path = 'output.txt'
with open(output_text_path, 'w') as text_file:
    text_file.write(extracted_text)
    text_file.write('\n\n')

# Close the PDF document
pdf_document.close()


# extracted_texts= ""
# for image in extracted_text:
#     # Convert the image data to a format that Tesseract can work with (e.g., PIL Image)
#     image_data = Image.frombytes(image.colorspace, image.getSize(), image.samples)

#     # Perform OCR to extract text from the image
#     text = pytesseract.image_to_string(image_data)

#     # Append the extracted text to the result
#     extracted_texts += text + "\n"