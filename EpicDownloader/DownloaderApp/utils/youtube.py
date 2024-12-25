import yt_dlp
import sys

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