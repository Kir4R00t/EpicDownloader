import instaloader
import requests

def insta(url):
    loader = instaloader.Instaloader(
        download_comments=False,
        download_geotags=False,
        download_pictures=False,
        download_video_thumbnails=False,
        save_metadata=False
    )
    
    # For example link it's this part 'DAI2BJRO8A6'
    shortcode = url.split('/')[-2]
    
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        print(f"Title: {post.caption}")

        # title = sanitize(post.caption) --> weirdly typed titles sometimes break this function
        title = shortcode
        vid_url = post.video_url
        
        response = requests.get(vid_url, stream=True)

        with open(f"{title}.mp4", 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Video downloaded successfully as {title}")

    except Exception as e:
        print(f'Something went wrong: {e}')