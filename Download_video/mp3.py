from pytube import YouTube


def Download(link):
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    try:
        print("The video is being downloaded....")
        stream.download()
        print("Downloaded successfully!")
    except:
        print("An error has occurred")


link = input("Enter a URL: ")
Download(link)
