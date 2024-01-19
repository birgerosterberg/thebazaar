from django.shortcuts import render

def faq_view(request):
    return render(request, 'faq/faq.html')