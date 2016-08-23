#!/usr/bin/env python


"""
interpretations of the options, some of them might be wrong:

format: bestaudio/best means first look for file with best audio quality,
        if not found then select best quality format represented by single 
        file with video and audio

"""

from __future__ import unicode_literals
import youtube_dl, sys, argparse

common_settings = {
        'continue': True,
        'embedthumbnail': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'ignoreerrors' : True,
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        #'proxy': 'http:proxy.iiit.ac.in:8080' #proxy
        'verbose': True
        }

#correct flac: something is wrong!!!!
flac = {
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac'
            }]
    }

mp3 = {
        #'audioformat' : "mp3",      # convert to mp3 
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }]
    }

mp3_playlist = {
        #'audioformat' : "mp3",      # convert to mp3 
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : False,        # only download single song, not playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }]
    }

mp4 = {
        #'extractaudio' : True,      # only keep the audio
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        'videoformat' : "mp4"      # convert to mp4
    }

mp4_playlist = {
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'noplaylist' : False,        # only download single song, not playlist
        'videoformat' : "mp4"      # convert to mp4 
    }

def download(args):
    options = {}
    if args['type'].endswith('p'):
        try:
            options.update({'playliststart': int(args['play_start'])})
        except:
            pass
        try:
            options.update({'playlistend': int(args['play_end'])})
        except:
            pass
    if args['type'] == 'flac':
        options.update(flac)
    elif args['type'] == 'mp3':
        options.update(mp3)
    elif args['type'] == 'mp3p':
        options.update(mp3_playlist)
    elif args['type'] == 'mp4':
        options.update(mp4)
    elif args['type'] == 'mp4p':
        options.update(mp4_playlist)

    options.update(common_settings)
    ydl = youtube_dl.YoutubeDL(options)
    r = ydl.extract_info(args['url'])

if __name__ == "__main__":
    arg_names = ['command', 'type', 'url', 'play_start', 'play_end']
    args = dict(zip(arg_names, sys.argv))
    download(args)
