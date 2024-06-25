# Compare images
import json
import numpy as np
from PIL import Image
import requests
import base64

def decode(encoded_img):
    aux_path = '/tmp/tmp.jpg'
    with open(aux_path, "wb") as f:
        f.write(base64.b64decode(encoded_img))
        f.close()
    out = np.array(Image.open(aux_path).convert('L'))
    return out

def ssim(imageA, imageB):
    
    # Implement a simplified version of the SSIM calculation
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2
    
    # Mean of the images
    mu1 = np.mean(imageA)
    mu2 = np.mean(imageB)
    
    # Variance of the images
    sigma1 = np.var(imageA)
    sigma2 = np.var(imageB)
    
    # Covariance
    sigma12 = np.cov(imageA.flat, imageB.flat)[0, 1]
    
    # SSIM computation
    ssim_score = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1**2 + mu2**2 + C1) * (sigma1 + sigma2 + C2))
    
    return ssim_score

def lambda_handler(event, context):
    
    img_bytes_1 = event["img1"]
    img_bytes_2 = event["img2"]
    
    img_1 = decode(img_bytes_1)
    img_2 = decode(img_bytes_2)
    
    ssim_score = ssim(img_1, img_2)
    
    # Set the return statement expected by AWS Lambda
    return 1 - ssim_score

# Image processing
import json
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import requests
import base64
import io

def decode(encoded_img):
    aux_path = '/tmp/tmp.jpg'
    with open(aux_path, "wb") as f:
        f.write(base64.b64decode(encoded_img))
        f.close()
    out = Image.open(aux_path)
    return out

def encode(img):
    aux_path = '/tmp/tmp.png'
    img.save(aux_path)
    
    with open(aux_path, "rb") as f:
        code = base64.b64encode(f.read())
        f.close()
    return code.decode("utf-8")

def lambda_handler(event, context):
    state = event['description']
    img_bytes = event["img"]
    img = decode(img_bytes)

    if state == 'gray':
        result_image = img.convert("L")
    elif state == 'hflip':
        result_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif state == 'vflip':
        result_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif state == 'contrast':
        enhancer = ImageEnhance.Contrast(img)
        result_image = enhancer.enhance(3)
    elif state == 'blur':
        result_image = img.filter(ImageFilter.BLUR)
    else:
        result_image = img
    
    # Create an in-memory binary stream to hold the image data
    result_buffer = io.BytesIO()
    # Save the resulting image to the in-memory stream as PNG (you can use a different format if needed)
    result_image.save(result_buffer, format="JPEG")
    # Get the binary image data from the buffer
    result_data = result_buffer.getvalue()
    # Encode the binary image data as base64
    result = base64.b64encode(result_data).decode("utf-8")
    # Close the in-memory stream
    result_buffer.close()
    
    return result
