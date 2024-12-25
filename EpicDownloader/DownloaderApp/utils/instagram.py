import instaloader
import requests
from django.http import HttpResponse


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

        response = requests.get(vid_url, stream=True)

        # Use an in-memory file to avoid saving on the server
        from io import BytesIO
        video_file = BytesIO()
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                video_file.write(chunk)

        # Create the HTTP response with the video file
        video_file.seek(0)  # Move to the beginning of the file
        response = HttpResponse(video_file, content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="{shortcode}.mp4"'

        return response

    except Exception as e:
        return HttpResponse(f"Something went wrong: {e}", status=400)
