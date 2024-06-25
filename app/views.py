from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image  # Requires Pillow library
import base64
from io import BytesIO
import boto3
import csv
from PIL import Image, ImageDraw, ImageFont
import io
import json
import requests

# Create your views here.

def compare(img1, img2):
    API_ENDPOINT = 'api_endpoint'

    # Encode image 1
    buffer1 = io.BytesIO()
    img1.save(buffer1, format="JPEG")
    encoded_image1 = base64.b64encode(buffer1.getvalue()).decode('utf-8')

    # Encode image 2
    buffer2 = io.BytesIO()
    img2.save(buffer2, format="JPEG")
    encoded_image2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')

    # Prepare data payload including transformations and image data
    data_payload = {
        'img1': encoded_image1,
        'img2': encoded_image2,
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(API_ENDPOINT, data=json.dumps(data_payload), headers=headers) 
    ssim = response.content.decode('utf-8')
    return ssim

def editAPI(img, desciption):
    API_ENDPOINT = 'api_endpoint'

    buffer1 = io.BytesIO()
    img.save(buffer1, format="JPEG")
    encoded_image = base64.b64encode(buffer1.getvalue()).decode('utf-8')

    # Prepare data payload including the base64-encoded description
    data_payload = {
        'img': encoded_image,
        'description': desciption,
    }

    # Encode the data payload as JSON
    json_payload = json.dumps(data_payload)

    headers = {'Content-Type': 'application/json'}
    response = requests.post(API_ENDPOINT, data=json.dumps(data_payload), headers=headers) 
    # Decode the base64-encoded byte string to obtain the binary image data
    image_data = base64.b64decode(response.content)
    # Create an in-memory binary stream (BytesIO) to hold the image data
    img_buffer = io.BytesIO(image_data)
    # Open the image from the in-memory stream using Pillow
    img = Image.open(img_buffer)
    return img

def home(request):
    return render(request, 'home.html', {})

def editing(request):
    return render(request, 'editing.html', {})

def maincontent(request):
    return render(request, 'maincontent.html', {})

def annotation(request):
    return render(request, 'annotation.html', {})

def similar(request):
    return render(request, 'similar.html', {})

def editing_r(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('imageFile')
        selected_transformation = request.POST.get('transformation')

        if uploaded_image:
            # Process the image (e.g., resize)
            image = Image.open(uploaded_image)
            processed_img = editAPI(img=image, desciption=selected_transformation) 
            
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            original = base64.b64encode(buffer.getvalue()).decode('utf-8')
            # Convert the resized image to base64
            buffer = BytesIO()
            processed_img.save(buffer, format="JPEG")
            processed = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            context = {
                'processed': processed,  
                'orignal': original,
            }
            return render(request, 'editing_result.html', context)

def maincontent_r(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('imageFile')
        if uploaded_image:
            source_bytes = uploaded_image.read()
            textract = boto3.client('textract', region_name='us-west-2',aws_access_key_id='aws_access_key_id'
                      , aws_secret_access_key='aws_secret_access_key')
            response = textract.detect_document_text(
                Document={
                    'Bytes': source_bytes
                }
            )
            text_extract = ''
            for item in response['Blocks']:
                if item['BlockType'] == 'LINE':
                    text_extract += item['Text'] + '\n'

            # Convert the resized image to base64
            image = Image.open(uploaded_image)
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

            context = {
                'text_extract': text_extract,
                'img_str': img_str,
            }
            return render(request, 'maincontent_result.html', context)
    return render(request, 'maincontent_result.html', {})

def annotation_r(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('imageFile')
        if uploaded_image:
            source_bytes = uploaded_image.read()

            # Convert the resized image to base64
            image = Image.open(uploaded_image)
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

            client = boto3.client('rekognition', region_name='us-west-2',
                        aws_access_key_id='aws_access_key_id', aws_secret_access_key='aws_secret_access_key')
            
            detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

            image = Image.open(io.BytesIO(source_bytes))
            draw = ImageDraw.Draw(image)

            labels_and_bboxes = {}

            for label in detect_objects['Labels']:
                for instances in label['Instances']:
                    if 'BoundingBox' in instances:
                        box = instances["BoundingBox"]
                        left = image.width * box['Left']
                        top = image.height * box['Top']
                        width = image.width * box['Width']
                        height = image.height * box['Height']
                        points = (
                                    (left,top),
                                    (left + width, top),
                                    (left + width, top + height),
                                    (left , top + height),
                                    (left, top)
                                )
                        labels_and_bboxes[label["Name"]] = {
                            "top_left": {"x": points[0][0], "y": points[0][1]},
                            "top_right": {"x": points[1][0], "y": points[1][1]},
                            "bottom_right": {"x": points[2][0], "y": points[2][1]},
                            "bottom_left": {"x": points[3][0], "y": points[3][1]}
                        }

                        draw.line(points, width=5, fill = "#69f5d9")
                        shape = [(left - 2, top - 35), (width + 2 + left, top)]
                        draw.rectangle(shape, fill = "#69f5d9")
                        font = ImageFont.truetype("arial.ttf", 30)
                        draw.text((left + 170, top - 30), label["Name"], font=font, fill='#000000')

            # Convert the processed image to base64
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            img_str_ = base64.b64encode(buffer.getvalue()).decode('utf-8')

            json_labels_and_bboxes = json.dumps(labels_and_bboxes, indent=4)

            context = {
                'original': img_str,
                'transformed': img_str_,  
                'labels': json_labels_and_bboxes,
            }
            return render(request, 'annotation_result.html', context)
    return render(request, 'annotation_result.html', {})

def similar_r(request):
    if request.method == 'POST':
        uploaded_image1 = request.FILES.get('image1')
        uploaded_image2 = request.FILES.get('image2')
        if uploaded_image1:
            # Process the image (e.g., resize)
            image1 = Image.open(uploaded_image1)
            image2 = Image.open(uploaded_image2)
            
            ssim = compare(image1, image2)

            # Convert the resized image to base64
            buffer = BytesIO()
            image1.save(buffer, format="JPEG")
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer = BytesIO()
            image2.save(buffer, format="JPEG")
            img_str_ = base64.b64encode(buffer.getvalue()).decode('utf-8')

            context = {
                'base64_encoded_image': img_str,  
                'base64_encoded_image_': img_str_,
                'result': ssim,
            }
            return render(request, 'similar_result.html', context)
    return render(request, 'similar_result.html', {})
