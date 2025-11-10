# TikTokLive for reading chat + WebDefaults for usage of user cookies
# pydub and sounddevice for playback, numpy to aid this
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent
from TikTokLive.client.web.web_settings import WebDefaults
from pydub import AudioSegment
import sounddevice as sd
import threading
import secret
import numpy as np


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
        threading.Thread(target=kw_to_sound(keyword), daemon=True).start()


# Path for audio files and name of device, can be found with sd.query_devices()
audio_path = r"C:\Users\usr\Documents\projects\tiktok\sounds\\"
output_device_name = "Headphones (Realtek(R) Audio), MME"


# Takes keyword, appends corresponding filename to path and calls play_sound with the full path
def kw_to_sound(kw):
    sound_command = keyword_dict.get(kw)
    path = audio_path + sound_command
    play_sound(path)


# Plays the sound effect from the chosen output device
def play_sound(path):
    audio = AudioSegment.from_file(path, format="mp3")
    samples = np.array(audio.get_array_of_samples()).astype(np.float32)
    samples = samples / np.max(np.abs(samples))
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))

    sd.play(samples, samplerate=audio.frame_rate, device=output_device_name, blocking=False)


client.run()
