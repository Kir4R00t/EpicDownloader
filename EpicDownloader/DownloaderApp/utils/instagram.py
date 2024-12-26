import instaloader
import requests
import os
from django.http import FileResponse, HttpResponse


def download(url):
    loader = instaloader.Instaloader(
        download_comments=False,
        download_geotags=False,
        download_pictures=False,
        download_video_thumbnails=False,
        save_metadata=False
    )
    
    # Extract shortcode from the URL
    shortcode = url.split('/')[-2]

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        vid_url = post.video_url

        temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        
        file_path = os.path.join(temp_dir, f"{shortcode}.mp4")

        response = requests.get(vid_url, stream=True)
        if response.status_code != 200:
            return HttpResponse("Failed to fetch video from Instagram", status=400)

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{shortcode}.mp4"'

        return response

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=400)