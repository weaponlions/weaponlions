from .forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('Done')
    else:
        form = UploadFileForm()
    return render(request, 'main.html', {'form': UploadFileForm()})

def handle_uploaded_file(f):
    with open('media/name3.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
