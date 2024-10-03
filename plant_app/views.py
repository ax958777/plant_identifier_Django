import os
import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64

genai.configure(api_key=settings.GEMINI_API_KEY)

def index(request):
    return render(request, 'plant_app/index.html')

@csrf_exempt
def identify_plant(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        if image_data:
            image_data = image_data.split(',')[1]
            image_bytes = base64.b64decode(image_data)

            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            response = model.generate_content([
                "Identify this plant and provide important information about it.",
                {"mime_type": "image/jpeg", "data": image_bytes}
            ])

            return JsonResponse({
                'success': True,
                'result': response.text
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
