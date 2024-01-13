from django.shortcuts import render
from models import YourModel

def your_view(request):
    data  = YourModel.objects.all(
    return render (request, 'your_app_templates.html' , {'data': data}(
    )
