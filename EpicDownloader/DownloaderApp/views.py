from django.shortcuts import render, HttpResponse
from .utils.download_video import download


def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print("Passing views")

        download(url) # Download video and send to user

    else:
        print("couldn't get url")
              
    return render(request, 'index.html')

