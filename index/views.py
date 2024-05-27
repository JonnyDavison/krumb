from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'index/index.html')


def findus(request):
    """
    A view to return the Fund Us page
    """
    return render(request, 'index/findus.html')

def about(request):
    """
    A view to return the Fund Us page
    """
    return render(request, 'index/about.html')