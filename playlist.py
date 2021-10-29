import subprocess
from pytube import Playlist

playlist_link = "http://youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN"

playlist = Playlist(playlist_link)

download_directory = r"C:\Users\23480\Desktop\ML"

for video in playlist.videos:
    print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(download_directory)