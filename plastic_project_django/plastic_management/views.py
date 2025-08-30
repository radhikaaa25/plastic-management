from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout 

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

@csrf_exempt
def login_register_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            #user exists and password is correct
            login(request, user) 
            return JsonResponse({'success': True, 'userId': user.id})
        else:
            #auth fail -> new user? register
            try:
                new_user = User.objects.create_user(username=username, password=password)
                login(request, new_user) 
                return JsonResponse({'success': True, 'userId': new_user.id})
            except Exception as e:
                return JsonResponse({'success': False, 'message': 'Username might be taken or password was incorrect.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def deposit_api(request):
    user_id = request.GET.get('userId')
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        profile.coins += 1
        profile.save()
        return HttpResponse(f"Bottle deposited! 🍼 You earned 1 coin. Total coins: {profile.coins} 🪙")
    except UserProfile.DoesNotExist:
        return HttpResponse("User not found")

def balance_api(request):
    user_id = request.GET.get('userId')
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        return HttpResponse(f"Your total balance: {profile.coins} 🪙")
    except UserProfile.DoesNotExist:
        return HttpResponse("User not found")