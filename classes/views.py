from django.shortcuts import render
from django.shortcuts import render

def book_a_class(request):
    return render(request, "classes/book_a_class.html")
