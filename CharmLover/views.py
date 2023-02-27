from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate

# Create your views here.
def WelcomePage(request):
    return render (request, 'index.html')

def LoginPage(request):
    return render (request, 'Login.html')
   
def SignupPage(request):
       return render (request, 'signup.html')
   
   
    #  if request.method=='POST':
    #   FName=request.POST.get('First_Name')   
    #   LName=request.POST.get('Last_Name')  
    #   Gender=request.POST.get('gender1')  
    #   DOB=request.POST.get('DOB')     
    #   country=request.POST.get('value')  
    #   PGender=request.POST.get('gender2')  
    #   uname=request.POST.get('Username')   
    #   email=request.POST.get('Email_address') 
    #   pass1=request.POST.get('password1') 
    #   pass2=request.POST.get('password2') 
    #  if pass2!=pass1:
    #      return HttpResponse('Your password and confirm password are not the Same!!!')
    #  else: 
    #     my_user=User.objects.create_user(FName,LName,Gender,DOB,country,PGender,uname,email,pass1)
    #     my_user.save()
    #     return redirect('login')
    

   
def AboutPage(request):
    return render (request, 'About.html')

def ContactUs(request):
    return render (request, 'ContactUs.html')
        
def Feedback(request):
    return render (request, 'feedback.html')

def Homepage(request):
    pass
    return render (request, 'home.html')

def freepage(request):
    return render(request, 'free.html')


def sendemail(request):
    if request.method == "POST":
        name = request.POST.get('Fullname')
        phone = request.POST.get('Number') 
        to = request.POST.get("toemail")
        # print(name,phone,to)   
        send_mail(
            "testing",
            name,
            settings.EMAIL_HOST_USER,
            ["tawanda.madziya@younglings.africa"]   
        )
        return render(
       request,
       'ContactUs.html',
       {
           'title':'LoveCharm Email'
       }
   )
    else:
        return render(
       request,
       'ContactUs.html',
       {
           'title':'send an email'
       }
   )
        
#    def logout(request):
#     pass