from . import youtube
from . import instagram

def download(url):
    if 'youtube' in url:
        youtube.download(url)
    elif 'instagram' in url:
        print("downloading instagram video")
        instagram.download(url)
    else:
        print(f"Cannot recognize origin of {url}")

    pass