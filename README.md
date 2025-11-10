# TokTokLiveChat_Soundboard
A python script to play sound effects when a certain command is typed in the users chat


## Features

- Connects to your TikTok Live chat using the **TikTokLive** Python library  
- Plays an MP3 or WAV sound when a viewer types a `!command`  
- Sends the sound through an audio device so TikTok Live Studio can capture it  
- Supports easy customization for more commands and sounds

## Requirements

- **Python 3.9+**
- A TikTok account that can go live
- TikTokLive library version **≥ 6.6.5**
- FFmpeg installed (for MP3 decoding)

## Installation
- Clone this repo
- Install dependencies if not already installed

## Dependencies
- Install dependencies with 'pip install TikTokLive pydub sounddevice'
- Download FFmpeg either with brew (macOS), apt (Linux) or from ffmpeg.org (Windows)

## Authentication and configuration
- TikTok might not verify the virtual device TikTokLive is using to look at comments (error DEVICE_BLOCKED)
  - If so install a cookie extension (Example Get cookies.txt LOCALLY), find cookies "s_v_web_id" and "ttwid" and import those into project
- Find audio device for output using sounddevice and change "output_device_name" accordingly
- Enter path for the directory of sound effects in "audio_path"
- Enter livestreaming accounts username in "username"
- Change "keyword_dict" according the needed commands and filenames with extensions. I believe both .mp3 files and .wav are supported, only tested with .mp3

## Usage
- Run from IDE or from terminal/shell by cd into the project path and running with "python main.py" alternatively "python3 main.py"


## Acknowledgments

This project uses [TikTokLive](https://github.com/isaackogan/TikTokLive/),
an open-source library licensed under the MIT License.
