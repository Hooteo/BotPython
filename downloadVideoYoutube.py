#pip install pytube
from pytube import YouTube
link= input("Enter link of video you want to download: ")
yt=YouTube(link)
#to stream all the format available
videos= yt.streams.all()
#get list of all format available
video= list(enumerate(videos))
for i in video:
	print(i)
print("enter the desired option to download the format: ")
dn_option= int(input("Enter the option: "))
dn_video= videos[dn_option]
dn_video.download()
print ("Download done!")
