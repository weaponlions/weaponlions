from django.shortcuts import render 
from django.http import HttpResponse
from .forms import FileNameForm
# Create your views here.


def index2(request):
    if request.method == 'POST':
        form = FileNameForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('Done')
    else:
        form = FileNameForm
    return render(request, 'main.html', {'form': form})
