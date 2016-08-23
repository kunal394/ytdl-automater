#!/usr/bin/env python

from __future__ import unicode_literals
import youtube_dl, sys, argparse

common_settings = {
        'continue': True,
        'fixup': 'detect_or_warn',  # Automatically correct known faults of the file.
        'ignoreerrors' : True,
        'outtmpl': '%(title)s.%(ext)s',     # name the file the title of the video
        'verbose': True,
        'writethumbnail': True,
        }

def contruct_flac():
    #TODO:debug flac!! something's wrong!!!!
    flac = {
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        }
    postprocessors = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
        }]
    return flac, postprocessors

def contruct_mp3():
    mp3 = {
        #'audioformat' : "mp3",      # convert to mp3 
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        }
    postprocessors = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        }]
    return mp3, postprocessors

def contruct_mp3_playlist():
    mp3_playlist = {
        #'audioformat' : "mp3",      # convert to mp3 
        'extractaudio' : True,      # only keep the audio
        'format': 'bestaudio/best', # choice of quality
        'noplaylist' : False,        # only download single song, not playlist
        }
    postprocessors = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        }]
    return mp3_playlist, postprocessors

def contruct_mp4():
    mp4 = {
        #'extractaudio' : True,      # only keep the audio
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'noplaylist' : True,        # only download single song, not playlist
        'videoformat' : "mp4",      # convert to mp4
        }
    return mp4

def contruct_mp4_playlist():
    mp4_playlist = {
        'format': 'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio/bestvideo[ext=mkv]+bestaudio/best', # choice of quality
        'noplaylist' : False,        # only download single song, not playlist
        'videoformat' : "mp4",     # convert to mp4 
        }
    return mp4_playlist

def download(args):
    global common_settings
    postprocessors = []

    if args['type'] == 'flac':
        options, p = contruct_flac()
    elif args['type'] == 'mp3':
        options, p = contruct_mp3()
    elif args['type'] == 'mp3p':
        options, p = contruct_mp3_playlist()
    elif args['type'] == 'mp4':
        options = contruct_mp4()
        p = []
    elif args['type'] == 'mp4p':
        options = contruct_mp4_playlist()
        p = []

    postprocessors.extend(p)
    postprocessors.append({
            'key': 'EmbedThumbnail',
            })
    options.update({'postprocessors' : postprocessors})

    if args['type'].endswith('p'):
        try:
            options.update({'playliststart': int(args['play_start'])})
        except:
            pass
        try:
            options.update({'playlistend': int(args['play_end'])})
        except:
            pass

    options.update(common_settings)


    print options
    ydl = youtube_dl.YoutubeDL(options)
    r = ydl.extract_info(args['url'])

if __name__ == "__main__":
    arg_names = ['command', 'type', 'url', 'play_start', 'play_end']
    args = dict(zip(arg_names, sys.argv))
    download(args)
