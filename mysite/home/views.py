from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/index.html', {'title': "Home"})


def test(request):
    return render(request, 'home/test.html')


