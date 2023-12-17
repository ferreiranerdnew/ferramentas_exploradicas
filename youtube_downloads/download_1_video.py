# Converter 3GPP para mp4
# https://www.online-convert.com/pt/result#j=c4332aec-0a3e-4c12-aa9e-52423f38ad91

#!pip install pytube

#pip install --upgrade pytube

#pip install git+https://github.com/baxterisme/pytube

from pytube import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=AZTV_uT2e68'
yt = YouTube(VIDEO_URL)
print(yt)
file ="F:\\videosyoutube\\"  #pasta que vai receber o video 

#video = yt.streams.filter(file_extension='mp4',only_video=True)
video = yt.streams.first()
video.download(file)