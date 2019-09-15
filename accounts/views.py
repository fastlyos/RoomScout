from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from utils import provinces
from .models import User
from .forms import PreferencesForm

@login_required(login_url="account_login")
def settings(request):
	preferences_form = PreferencesForm()
	provs = provinces.get_provinces()
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		if request.POST['first_name']:
			user.first_name = str(request.POST['first_name'])
		if request.POST['last_name']:
			user.last_name = str(request.POST['last_name'])
		if request.POST['city']:
			user.city = str(request.POST['city'])
		if request.POST['province']:
			user.province = request.POST['province']
		if request.POST['age']:
			user.age = request.POST['age']
		if request.POST['gender']:
			user.gender = request.POST['gender']
		if request.POST['phone_number']:
			user.phone_number = request.POST['phone_number']
		user.save()
		messages.success(request, 'Your settings have been saved!.')
		return redirect('settings')
	else:
		return render(request, 'account/settings.html', {'provinces': provs, 'preferences_form':preferences_form})
