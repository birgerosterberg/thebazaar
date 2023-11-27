from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return to the bazaar page """

    return render(request, 'bazaar/bazaar.html')
