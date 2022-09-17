from django.http import HttpResponse
from django.shortcuts import render
from .forms import Downloads
import pytube
# Create your views here.


def home(request):
    download = Downloads()
    if request.method == 'POST':
        download = Downloads(request.POST)
        if download.is_valid():
           link =  download.cleaned_data['link']
    # link = input("enter your youtube url: ")
        yt = pytube.YouTube(link)
        yt.streams.filter(res="720p").first().download()
        return HttpResponse('your video is downloaded')
    context = {'download': download,}
    return render(request, 'home.html/', context)
