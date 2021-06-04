from django.shortcuts import render, HttpResponse, redirect
from .models import Hire_me
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'mycv/port.html')

def hire_me(request):
	if request.method == "POST":
		name = request.POST.get("name", '')
		email = request.POST.get("email", '')
		msg = request.POST.get("msg", '')

		contact = Hire_me(h_name=name, h_email=email, h_msg=msg)
		contact.save()

		messages.success(request, "Thank you for your interest, You will get your reply ASAP!")
		return redirect('/')

