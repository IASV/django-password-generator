from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(reqeust):
    return render(reqeust, 'generator/home.html')

def generate(request):
    return render(request, 'generator/password.html')