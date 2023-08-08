from django.shortcuts import render
from .utils import generate_caption
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def process_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        generated_caption = generate_caption(image)
        return JsonResponse({'caption': generated_caption})
    else:
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')

