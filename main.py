import glob
import sys
import os
from pydub import AudioSegment

combined = AudioSegment.empty()

text = input('Text to generate: ')

audiopath = 'audio/'

letters = []

for i in text:
    if i.isalpha() or i.isnumeric():
        letters.append(i)

for i in range(len(letters)):
    letters[i] = audiopath + letters[i].upper() + '.wav'

# debugging
# print(letters)

audio = []

for letter in letters:
    audiofilename = AudioSegment.from_wav(letter)
    audio.append(audiofilename)

for i in audio:
    combined += i
combined.export('generated.wav', format='wav')

# https://stackoverflow.com/questions/51434897/how-to-change-audio-playback-speed-using-pydub
def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
