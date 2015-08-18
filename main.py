#!/usr/bin/env python

# a script to collect lists of all songs played by a pandora station
# use bs4
# create a directory if there is not one
# create a station file if there is not one
# list station songs to one file per station

# requires pianobar

# Jared Henry Oviatt

from bs4 import BeautifulSoup
import os
import sys

LIST_DIR_PATH = "~/code/py/pan_list/"

station = "none"
song = "none"

def check_dir():
  command = "ls " + LIST_DIR_PATH + " | grep ' pandora_song_lists '"
  if not os.system(command):
    return
  else:
    os.system('mkdir pandora_song_lists')
    return

def new_file():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  f = open(songs_path + station, 'w')
  f.write('This is a list of all songs played on Pandora station ' + station)
  f.close()
  return

def check_file():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  command = "ls " + songs_path + " | grep ' " + station + " '"
  if not os.system(command):
    return 0
  else:
    new_file():
    return

def check_songs():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  f = open(songs_path + station, 'r')
  if song in f.read():
    return 1
  return 0
  

def add_song():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  f = open(songs_path + station, 'a')
  f.write(song)
  f.close()
  return


def check_sta():

def parse_output():

def main(argv):
# check for -h option
# check for -s option for station list # or get station list another way

# start pianobar, pipe to output file

# parse output file 
  return

if __name__ == '__main__':
  main(sys.argv[])
