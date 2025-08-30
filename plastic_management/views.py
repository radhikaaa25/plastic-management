from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile, QRCode
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def qr_scanner_page(request):
    return render(request, 'qr_scanner.html')

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

@csrf_exempt
def qr_scan_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        qr_code = data.get('qrCode')
        user_id = data.get('userId')
        
        try:
            profile = UserProfile.objects.get(user__id=user_id)
            
            # Check if QR code exists and is not used
            try:
                qr_obj = QRCode.objects.get(code=qr_code)
                
                if qr_obj.is_used:
                    return JsonResponse({
                        'success': False, 
                        'message': 'This QR code has already been used!'
                    })
                
                # Mark QR code as used and award points
                qr_obj.is_used = True
                qr_obj.used_by = profile
                qr_obj.used_at = datetime.now()
                qr_obj.save()
                
                # Award points to user
                profile.coins += 10  # 10 points per bottle
                profile.total_bottles += 1
                profile.save()
                
                return JsonResponse({
                    'success': True,
                    'message': f'Bottle deposited successfully! 🍼 You earned 10 points. Total: {profile.coins} points',
                    'coins': profile.coins,
                    'totalBottles': profile.total_bottles
                })
                
            except QRCode.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid QR code! Please scan a valid bottle QR code.'
                })
                
        except UserProfile.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'User not found'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def deposit_api(request):
    user_id = request.GET.get('userId')
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        profile.coins += 1
        profile.total_bottles += 1
        profile.save()
        return HttpResponse(f"Bottle deposited! 🍼 You earned 1 coin. Total coins: {profile.coins} 🪙")
    except UserProfile.DoesNotExist:
        return HttpResponse("User not found")

def balance_api(request):
    user_id = request.GET.get('userId')
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        return HttpResponse(f"Your total balance: {profile.coins} points")
    except UserProfile.DoesNotExist:
        return HttpResponse("User not found")

def stats_api(request):
    user_id = request.GET.get('userId')
    try:
        profile = UserProfile.objects.get(user__id=user_id)
        return JsonResponse({
            'coins': profile.coins,
            'totalBottles': profile.total_bottles,
            'joinedDate': profile.created_at.strftime('%B %Y')
        })
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'})

# Admin endpoint to generate QR codes (for testing)
@csrf_exempt
def generate_qr_codes(request):
    if request.method == 'POST':
        count = int(request.POST.get('count', 10))
        codes = []
        
        for i in range(count):
            import random
            import string
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            qr = QRCode.objects.create(code=code)
            codes.append(code)
        
        return JsonResponse({
            'success': True,
            'message': f'Generated {count} QR codes',
            'codes': codes
        })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})