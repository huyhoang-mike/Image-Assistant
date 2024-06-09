import easyocr
import cv2

def ocr():
    reader = easyocr.Reader(['en'])  # Specify the language(s) you want to enable (e.g., 'en' for English)
    filename = 'C:/DISK (D)/HCMUT/OTH/SoSe/4. Cloud_Computing/Cloud_Computing_HuyHoangNguyen_3421125/Demonstration/Implementation/editjpg.jpg'
    image = cv2.imread(filename)  # Read the image
    result = reader.readtext(image)  # Perform OCR
    texts = []
    # Print the recognized text
    for bbox, text, confidence in result:
        texts.append(text)
    return texts

print(ocr())