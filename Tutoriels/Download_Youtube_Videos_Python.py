#import pytube lybrary to download the video
import pytube

#Ask for the url of video
url = input("Entrer une url video: ")
#we can take path as well, just uncomment the following line
#path = input("Enter path of storage")

#specify the storage path of video
path="E:"

#magic Line to download the video
pytube.YouTube(url).stream.get_highest_resolution().download(path)