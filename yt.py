import pytube
import os
import pytubemp3
import time
#YouTube(video_url).streams.filter(only_audio=True).first().download()


def download_mp4(url:str):
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
    start = time.time()
    video = pytube.YouTube(url)
    video.streams.get_highest_resolution().download(downloads)
    return (time.time() - start)

def download_mp3(url:str):
    downloads = f"{os.getenv('USERPROFILE')}\\Downloads"
    pass

def get_info(url:str):
    video = pytube.YouTube(url)
    title = video.title
    length = video.length
    views = video.views

    secs = length%60
    mins = int(length/60)
    length = str(mins) + ":" + str(secs)
    return [title,length,views]
