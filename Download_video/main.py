from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print("The video is being downloaded....")
        youtubeObject.download()
        title_video = youtubeObject.title
        print("Title of the video is {}\n".format(title_video))
        print("Download was completed successfully")

    except:
        print("An error has occurred")


link = input("Enter the YouTube URL: ")
Download(link)

# Explanation
"""
The youtubeObject = youtubeObject.streams.get_highest_resolution() command will automatically download the highest resolution available.
Then I implemented the Try and Except to return an error message if the download fails – else it will print out that the download is completed successfully.
"""
