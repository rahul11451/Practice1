import pdf2image
from PIL import Image
import pytesseract

image = pdf2image.convert_from_path('sample.pdf')
for pagenumber, page in enumerate(image):
    detected_text = pytesseract.image_to_string(page, lang="eng")
    print(detected_text)