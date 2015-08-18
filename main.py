#!/usr/bin/env python

# a script to collect lists of all songs played by a pandora station
# use bs4
# create a directory if there is not one
# create a station file if there is not one
# list station songs to one file per station

# requires pianobar

# Jared Henry Oviatt

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
    new_file()
    return

def check_songs():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  f = open(songs_path + station, 'r')
  if song in f.read():
    return 1
  return 0
  

def add_song():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  if check_songs():
    return
  f = open(songs_path + station, 'a')
  f.write(song)
  f.close()
  return

def get_station():
  return

def parse_output():
  return

def start_pianobar(email, password):
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  os.system('pianobar >> ' +  songs_path + 'raw.txt')
  # login
  sys.stdout.write(email+'\n')
  sys.stdout.write(password)
  return

def choose_station():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  os.system('cat ' + songs_path + 'raw.txt')
  return

def quit_pianobar():
  return

def main(argv):
# check for -h option
# # args, etc

# start pianobar, pipe to output file
  start_pianobar(argv[1], argv[2])
  choose_station()
 
  close = input('\npress ENTER to quit\n')
  sys.stdout.write('q\n')

# parse output file 
  return

if __name__ == '__main__':
  main(sys.argv)
