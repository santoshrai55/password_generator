from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'generator_app/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        characters.extend(uppercase)

    if request.GET.get('numbers'):
        uppercase = list("0123456789")
        characters.extend(uppercase)

    if request.GET.get('special'):
        uppercase = list("!@#$%*()-+=")
        characters.extend(uppercase)

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator_app/password.html', {'password': thepassword})
