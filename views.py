from django.shortcuts import render

def home(request):
    context = {
        'title': 'Python Site Test',
           
        }
    return render(request, 'home.html', context)

def about (request):
    context = {
        'title': 'About Us',
    }

    return render(request, 'about.html', context)