from django.shortcuts import render
from .models import Library

def library_detail(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'library_detail.html', {'library': library})