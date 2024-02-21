from django.shortcuts import render,redirect
from .models import user_details
from django.http import HttpResponse
from django.http import JsonResponse

def registration_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user= user_details.objects.create(username=username,email=email,password=password)
        new_user.save()
        return redirect('registration_successful')
    return render(request,'register_page.html')

def registration_success(request):
    return render(request,'registration_successful.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = user_details.objects.get(username=username, password=password)
            return redirect("home_page")
        except user_details.DoesNotExist:
            return HttpResponse("invalid username & password")
    return render(request,'login_page.html')

def home_page(request):
    
    return render(request,"home_page.html")

def ai_page(request):
    return render(request,"ai.html")
def cloud_page(request):
    return render(request,"cloud.html")
def lmw_page(request):
    return render(request,"lmw.html")
def contact_page(request):
    return render(request,"contact.html")
# Create your views here.


