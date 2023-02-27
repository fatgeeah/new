from django.shortcuts import render

def welcomepage(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'Login.html')

def aboutus(request):
    return render(request, 'About.html')

def contactus(request):
    return render(request, 'ContactUs.html')

def feedback(request):
    return render(request, 'feedback.html')