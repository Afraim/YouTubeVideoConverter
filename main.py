from pytube import YouTube as yt
import os

#Clear consol everytime the app runs
os.system('cls')

def YouTubeInfo(URL):
    while (True):
        os.system("cls")
        video = yt(URL)
        ch = input("1. Video Title\n2. Convert to mp3\n3. Download Video (Low res)\n4. Download Video (High res)\n5. New URL\n0. Exit\n\t:")

        if ch=="1":
            print("Title: ",video.title) #prints the title of the video
        elif ch =="2":
            myvideo = video.streams.get_audio_only()  #records the audio of the file
            downloaded_file = myvideo.download()      #myvideo.download downloads a mp4 file
            base, ext = os.path.splitext(downloaded_file) #file separated in to base and extention
            new_file = base + '.mp3' #extension changed from mp4 to mp3
            os.rename(downloaded_file, new_file) #rename the main output file
            print("Successful")            
        elif ch =="3":
            myvideo = video.streams.get_lowest_resolution()
            myvideo.download()
            print("Successful")
        elif ch =="4":
            myvideo = video.streams.get_highest_resolution()
            myvideo.download()
            print("Successful")
        elif ch =="4":
            url = input("Enter New URL: ")
            video = yt(url)
            YouTubeInfo()
        elif ch =="0":
            os._exit(0)
        else :
            YouTubeInfo()

        
        os.system("pause")

    
def MAIN():
    #input url
    url = input("Input URL: ")
    try:
        os.system("cls")
        YouTubeInfo(url)
    except Exception:
        print("Something went wrong. Please check internet connection. Add \"https//\" in the URL.\n Please try again or press Q to exit")
        ch = input("...Press any key to continue...")
        if ch == "Q" or ch == "q":
            os.system("cls")
            MAIN()
        else:
            os._exit(0)

MAIN()
