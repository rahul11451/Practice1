# import PyPDF2

# # Replace this with the path to your PDF file
# pdf_file_path = 'sample.pdf'

# def read_pdf(file_path):
#     with open(file_path, 'rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Check if the PDF file can be read
#         if not pdf_reader.is_encrypted:
#             pdf_text = ''

#             # Read each page in the PDF
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 pdf_text += page.extract_text()
#                 print(pdf_text)

#             return pdf_text

# # if __name__ == '__main':
# print('nen')
# text = read_pdf(pdf_file_path)
# print(text)

from pdf2image import convert_from_path
import pytesseract

# Replace this with the path to your input PDF file
input_pdf_path = 'sample.pdf'

# Replace this with the path to your output text file
output_text_path = 'output.txt'

def convert_pdf_to_text_with_ocr(pdf_path, text_path):
    images = convert_from_path(pdf_path)
    with open(text_path, 'w') as text_file:
        for page_num, image in enumerate(images, 1):
            text = pytesseract.image_to_string(image, lang='eng', config=r'--psm 6 --oem 3')
            text_file.write(f'Page {page_num}:\n\n')
            text_file.write(text)
            text_file.write('\n\n')

if __name__ == '__main__':
    convert_pdf_to_text_with_ocr(input_pdf_path, output_text_path)
    print(f'Text extracted from {input_pdf_path} and saved to {output_text_path}')


# import pytesseract
# from PIL import Image
# import cv2

# # Open the image file
# # image = Image.open('demo_image.jpg')
# image = cv2.imread('demo_image.jpg')
# # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# # image = cv2.medianBlur(image, 5)
# print(image)
# # Perform OCR using PyTesseract
# # text = pytesseract.image_to_string(image)

# # Replace this with the path to your output text file
# output_text_path = 'output.txt'

# with open(output_text_path, 'w', encoding='utf-8') as text_file:
#     text = pytesseract.image_to_string(image, lang="eng", config=r'--psm 6')
#     # text_file.write(f'Page {page_num}:\n\n')
#     text_file.write(text)
#     text_file.write('\n\n')
# # Print the extracted text
# print(text)