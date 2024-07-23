from django.shortcuts import render
from products.models import Gallery

def index(request):
    """
    A view to return the index page
    """
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
}
    return render(request, 'index/index.html', context)


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