import os
from tkinter import *
from yt_dlp import YoutubeDL


        
def download_video():
    # Get the video URL from the entry field
    video_url = video_url_entry.get()

    # Choose the download format
    format_choice = format_choice_var.get()
    
    if (format_choice == 'mp4'):
        # Create a YoutubeDL instance
        ydl = YoutubeDL()

        # Set options for downloading
        options = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'outtmpl': os.path.expanduser('~/Documents/Playlist/%(title)s.%(ext)s'),
        }

        # Download the video
        with ydl:
            ydl.download([video_url])

    elif (format_choice == 'mp3'):
        # Convert the downloaded video to MP3
        mp3_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.expanduser('~/Documents/Playlist/%(title)s.%(ext)s'),
        }

        # Create a new YoutubeDL instance for MP3 conversion
        mp3_ydl = YoutubeDL(mp3_options)

        # Download the audio as MP3
        with mp3_ydl:
            mp3_ydl.download([video_url])

        status_label.config(text="El video se ha convertido a MP3 exitosamente.") 

# Create the main window
window = Tk()
window.title("YouTube Downloader")

# Create a label and entry field for the video URL
video_url_label = Label(window, text="Ingresa la URL del video:")
video_url_label.pack()
video_url_entry = Entry(window, width=50)
video_url_entry.pack()

# Create radio buttons for format choice
format_choice_var = StringVar()
mp4_radio = Radiobutton(window, text="MP4", variable=format_choice_var, value="mp4")
mp4_radio.pack()
mp3_radio = Radiobutton(window, text="MP3", variable=format_choice_var, value="mp3")
mp3_radio.pack()

# Create a button to initiate the download
download_button = Button(window, text="Descargar", command=download_video)
download_button.pack()




# Create a label for status messages
status_label = Label(window, text="")
status_label.pack()

# Run the main window loop
window.mainloop()