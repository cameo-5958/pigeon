from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from .forms import UploadFileForm
from .models import UploadedFile

# Create your views here.

def download_file(request, filename):
    try:
        instance = UploadedFile.objects.get(file__endswith=filename)
    except UploadedFile.DoesNotExist:
        raise Http404("File not found in database")

    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    
    if os.path.exists(filepath):
        return FileResponse(open(filepath, "rb"), as_attachment=True, filename=instance.file_name)

    else:
        raise Http404("File does not exist")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect(reverse('files:upload_success') + f'?filename={instance.file}')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    filename = request.GET.get('filename')
    return render(request, 'success.html', {'filename': filename})
