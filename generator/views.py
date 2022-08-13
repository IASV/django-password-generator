from django.shortcuts import render
# from django.http import HttpResponse
from random import choice

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(reqeust):
    return render(reqeust, 'generator/home.html')

def generate(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    length = int(request.GET.get('lenght'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for x in range(length):
        generated_password += choice(characters) 
    
    return render(request, 'generator/password.html', {'password': generated_password})