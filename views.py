from django.shortcuts import render
from .models import FoodItem

def home(request):
    user_mood = request.GET.get('mood', 'happy')
    # Database se us mood ke saare items nikalo
    items = FoodItem.objects.filter(mood=user_mood)
    
    context = {
        'mood': user_mood,
        'items': items
    }
    return render(request, 'index.html', context)