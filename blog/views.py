from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return None


def post_details(request):
    pass
