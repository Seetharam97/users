import json
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		password2 = request.POST.get('password2')

		if(password == password2):
			if User.objects.filter(username= username).first():
				return JsonResponse({'status': 'failure', 'messages': messages.error(request,'That username is taken')})
			else:
				if User.objects.filter(email= email).first():
					return JsonResponse({'status': 'failure', 'messages': messages.error(request,'That email is taken')})
				else:
					user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
					user.save()
					return JsonResponse({'status': "success", 'messages': 'Registration successfully'})
		else:
			return JsonResponse({'status': 'failure', 'messages': messages.error(request,'Password do not match')})
	else:
		return JsonResponse({'status': 'failure', 'messages': "Something went wrong"})

@csrf_exempt
def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username = username, password =password)

		if user is not None:
			auth.login(request, user)
			return JsonResponse({'status': 'success', 'messages': 'successfully login'})
		else:
			return JsonResponse({'status': 'failure', 'messages': 'Invalid username or password'})
	else:
		return JsonResponse({'status': 'failure', 'messages': "Something went wrong"})

@csrf_exempt
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return JsonResponse({'status': 'success', 'messages': 'successfully logout'})
	else:
		return JsonResponse({'status': 'failure', 'messages': "Something went wrong"})
