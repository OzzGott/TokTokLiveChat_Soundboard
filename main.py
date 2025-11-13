# TikTokLive for reading chat + WebDefaults for usage of user cookies
# pydub and sounddevice for playback, numpy to aid this
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent
from TikTokLive.client.web.web_settings import WebDefaults
import secret
import pygame.mixer as mixer

# Initialize the pygame mixer with set values, 16 sounds can be played at once
mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
mixer.set_num_channels(16)

# Path for audio files and name of device, can be found with sd.query_devices()
audio_path = r"C:\Users\usr\Documents\projects\tiktok\sounds\\"
output_device_name = "Headphones (Realtek(R) Audio), MME"

# User cookies in dictory imported from "secret" python file - not necessarily needed
ttwid = secret.ttwid
s_v_web_id = secret.s_v_web_id
cookies = {
    "s_v_web_id": s_v_web_id,
    "ttwid": ttwid,
}
WebDefaults.web_client_cookies = cookies

# Set username for the livestreaming TikTok user
username = "USER"
client = TikTokLiveClient(unique_id=username)

# Expandable dictionary to point from chat message to the name of the sound effect
keyword_dict = {
    "!bruh": "bruh.mp3",
    "!run": "cartoon_run.mp3",
    "!guitar": "bad-to-the-bone.mp3",
    "!yoda": "lego_yoda.mp3",
    "!lego": "lego_break.mp3",
}


# Comment checker - Looks at every comment and checks for keyword - if found, points keyword to kw_to_sound
@client.on(CommentEvent)
def on_comment(event: CommentEvent):
    if event.comment.strip().lower() in keyword_dict:
        keyword = event.comment.strip().lower()
        kw_to_sound(keyword)


# Takes keyword, appends corresponding filename to path and calls play_sound with the full path
def kw_to_sound(kw):
    sound_command = keyword_dict.get(kw)
    path = audio_path + sound_command
    play_sound(path)


# Plays the sound effect from the chosen output device
def play_sound(path):
    sound = mixer.Sound(path)
    sound.play


client.run()
