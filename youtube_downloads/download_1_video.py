# Converter 3GPP para mp4
# https://www.online-convert.com/pt/result#j=c4332aec-0a3e-4c12-aa9e-52423f38ad91

#!pip install pytube

#pip install --upgrade pytube

#pip install git+https://github.com/baxterisme/pytube

from pytube import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=wbV2KX6iIO8'
yt = YouTube(VIDEO_URL)
print(yt)
file ="K:\\000015.dowCanaisYoutube\\Trey Codes\\videos"  #pasta que vai receber o video 

#video = yt.streams.filter(file_extension='mp4',only_video=True)
video = yt.streams.first()
video.download(file)

# RF ESTUDO SUPER MARIO EM FLUTTER REPRODUZIR BAIXAR VIDEO E GIT    feito download em 17/12/2023
 #   Recreating Super Mario Bros. with Flutter & Flame | Step-by-Step Tutorial | Part Two 🍄 🎮 🔥
# https://www.youtube.com/watch?v=wbV2KX6iIO8