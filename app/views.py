from django.shortcuts import render
from app.models import Registration
from app.forms import RegistrationForm


# Create your views here.
def homeview(request):
	return render(request,"app/home.html")


def regview(request):
	f=Registration.objects.all()
	return render(request,"app/reg.html",{"m":f})

def createview(request):
	form=RegistrationForm()
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,"app/create.html",{"emp":form})