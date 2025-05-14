from django.shortcuts import render
from .models import ReadingSubmission
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ReadingSubmission.objects.create(
            name=data.get('name'),
            topic=data.get('topic'),
            dob=datetime.strptime(data.get('dob'), '%Y-%m-%d').date(),
            email=data.get('email')
        )
        return JsonResponse({'status': 'success'})
    return render(request, 'index.html')
