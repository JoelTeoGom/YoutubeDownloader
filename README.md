# YouTube Downloader

This is a Python script that allows you to download videos and playlists from YouTube using the `yt-dlp` library and a Tkinter GUI. It provides a simple and user-friendly interface for downloading videos in both MP4 and MP3 formats.

## Features

- Download videos and playlists from YouTube.
- Supports downloading in MP4 and MP3 formats.
- Automatic conversion of downloaded videos to MP3 format.
- Customizable download location.
- User-friendly GUI with entry fields and radio buttons.

## Requirements

- Python 3.x
- `yt-dlp` library
- Tkinter library (usually included in Python installations)

## How to Use

1. Make sure you have Python 3.x installed on your system.
2. Install the `yt-dlp` library by running the following command:
   ```
   pip install yt-dlp
   ```
3. Save the Python script to your desired location.
4. Open a terminal or command prompt and navigate to the directory where the script is saved.
5. Execute the script by running the following command:
   ```
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the Python script file.
6. The GUI window will open.
7. Enter the URL of the video or playlist you want to download in the provided field.
8. Select the desired download format (MP4 or MP3) using the radio buttons.
9. Click the "Download" button to initiate the download process.
10. The downloaded video or audio file will be saved in the specified location (by default, in the "~/Documents/Playlist" directory).
11. Status messages will be displayed in the GUI, indicating the progress and completion of the download.

## Creating a Shortcut (Linux)

To create a shortcut for the YouTube Downloader script on your Linux system, you can use a `.desktop` file. Here's an example:

```plaintext
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download videos from YouTube
Exec=python3 /path/to/youtube_downloader.py
Icon=/path/to/icon.png
Terminal=false
Categories=AudioVideo;Network;
```

Make sure to modify the following fields according to your system:

- `Exec`: Replace `/path/to/youtube_downloader.py` with the actual path to the Python script.
- `Icon`: Replace `/path/to/icon.png` with the actual path to the icon image file.

To create the shortcut:

1. Open a text editor and paste the above code into a new file.
2. Save the file with a `.desktop` extension (e.g., `youtube_downloader.desktop`).
3. Move the `.desktop` file to either `~/.local/share/applications` (for a user-specific shortcut) or `/usr/share/applications` (for a system-wide shortcut). You may need administrative privileges to copy it to the latter directory.
4. The YouTube Downloader shortcut should now appear in your application launcher or menu, ready to be executed by clicking on it.

Please note that this `.desktop` file is specific to Linux systems and may not work on other operating systems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

This script is for personal use only. Please ensure that you comply with the terms of service of YouTube and respect the intellectual property rights of the content creators when using this tool. The script is provided as-is, without any warranties or guarantees of any kind. Use it at your own risk.