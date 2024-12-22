from pytube import YouTube
import instaloader
import requests
import yt_dlp
import sys
import re

# Example links
# Insta - https://www.instagram.com/reel/DAI2BJRO8A6/?igsh=eDAycmY3NDFqOGd4
# Yt - https://www.youtube.com/watch?v=gWiMABiMIoM&ab_channel=TechFox
# Reddit - https://www.reddit.com/r/weed/comments/1go8ij6/do_you_smoke_to_sleep_at_night/

# Remove chars that windows considers illegal in a file name
def sanitize(string):
    return re.sub(r'[<>:"/\\|?*]', '', string)

class YTDLPLogger:
    def debug(self, msg):
        pass # Ignore debug msgs

    def warning(self, msg):
        print(f"WARNING: {msg}")

    def error(self, msg):
        print(f"ERROR: {msg}")
  
def youtube(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'best',
        'quiet': True,
        'logger': YTDLPLogger(),
        'out': sys.stdout,
        'error': sys.stderr
    }
   
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        print(f"Download failed: {e}")

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

def reddit(url):
    print("Reddit")

def spotify(url):
    print("Spotify")

def soundcloud(url):
    print("SoundCloud")

def main():
    url = str(input("Giv a link: "))
    youtube(url)

if __name__ == "__main__":
    main()
