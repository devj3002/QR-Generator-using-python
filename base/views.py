from django.shortcuts import render
import pyqrcode
import png
import os
from django.http import HttpResponse
from django.conf import settings

def home(request):
    if request.method=="POST":
        input_text=request.POST["input_text"]
        qr = pyqrcode.create(str(input_text))
        qr.png("media/code.png", scale=6)
        file_path=os.path.join(settings.MEDIA_ROOT + "code.png")
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename=code.png'
            return response
    return render(request,"base/home.html")