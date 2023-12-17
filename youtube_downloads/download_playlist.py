#!pip install pytube

from pytube import Playlist

file ="K:\\000015.dowCanaisYoutube\\Mo Malaka  Programador off line\\videos" #diretorio para salvar os videos

playlist = Playlist('https://www.youtube.com/watch?v=B3DVyCRe4k8&list=PLCB4518Yqs_JjlA3820tzL1169qgcCdKS') #URL da playlist

print('Number of videos in playlist: %s' % len(playlist.video_urls))

for video in playlist.videos:
    video.streams.first().download(file)