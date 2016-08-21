#!/usr/bin/env python


"""
interpretations of the options, some of them might be wrong:

format: bestaudio/best means first look for file with best audio quality,
        if not found then select best quality format represented by single 
        file with video and audio

"""

from __future__ import unicode_literals
import youtube_dl, sys

#correct flac: something is wrong!!!!
flac = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestaudio/best', # choice of quality
        'ignoreerrors' : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac'
            }],
        'extractaudio' : True,      # only keep the audio
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'noplaylist' : True,        # only download single song, not playlist
        #'proxy': 'http:proxy.iiit.ac.in:8080' #proxy
    }

mp3 = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestaudio/best', # choice of quality
        'ignoreerrors' : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        'extractaudio' : True,      # only keep the audio
        #'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'noplaylist' : True,        # only download single song, not playlist
        #'proxy': 'http:proxy.iiit.ac.in:8080' #proxy
    }

mp4 = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'ignoreerrors' : True,
        #'extractaudio' : True,      # only keep the audio
        'videoformat' : "mp4",      # convert to mp4
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'noplaylist' : True,        # only download single song, not playlist
    }

mp3_playlist = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestaudio/best', # choice of quality
        'ignoreerrors' : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
        'extractaudio' : True,      # only keep the audio
        #'audioformat' : "mp3",      # convert to mp3 
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'noplaylist' : False,        # only download single song, not playlist
    }

mp4_playlist = {
        'verbose': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'ignoreerrors' : True,
        'videoformat' : "mp4",      # convert to mp4 
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'noplaylist' : False,        # only download single song, not playlist
    }

def down(url, t):
    if t == 'flac':
        options = flac
    elif t == 'mp3':
        options = mp3
    elif t == 'mp3p':
        options = mp3_playlist
    elif t == 'mp4':
        options = mp4
    elif t == 'mp4p':
        options = mp4_playlist
    ydl = youtube_dl.YoutubeDL(options)
    r = ydl.extract_info(url)

if __name__ == "__main__":
    url = sys.argv[1]
    t = sys.argv[2]
    down(url, t)
