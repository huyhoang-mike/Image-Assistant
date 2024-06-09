from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image  # Requires Pillow library
import base64
from io import BytesIO
# Create your views here.

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
        if uploaded_image:
            # Process the image (e.g., resize)
            image = Image.open(uploaded_image)
            resized_image = image.resize((200, 200))  # Example: Resize to 300x200
            
            # Convert the resized image to base64
            buffer = BytesIO()
            resized_image.save(buffer, format="JPEG")
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer = BytesIO()
            image.save(buffer, format="JPEG")
            img_str_ = base64.b64encode(buffer.getvalue()).decode('utf-8')

            context = {
                'base64_encoded_image': img_str,  
                'base64_encoded_image_': img_str_,
            }
            return render(request, 'editing_result.html', context)

def maincontent_r(request):
    return render(request, 'maincontent_result.html', {})

def annotation_r(request):
    return render(request, 'annotation_result.html', {})

def similar_r(request):
    return render(request, 'similar_result.html', {})