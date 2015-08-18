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

LIST_DIR_PATH = "/home/jho/code/py/pan_list/"

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

def add_song():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  if check_songs():
    return
  f = open(songs_path + station, 'a')
  f.write(song)
  f.close()
  return

def check_songs():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  f = open(songs_path + station, 'r')
  if song in f.read():
    return 1
  return 0
  

def parse_output(filename):
  f = open(filename, 'r')
  raw = f.readlines()
  f.close
  
 # os.remove(filename)
  
  for line in raw:
    if '|>' not in line[:2]:
      continue
    if 'Station' in line[4:14]:
      station = line
      lsplit = station.split('"')
      station = lsplit[1]
      for i in station:
        if i == ' ':
          i = '_'
      check_file()
    else:
      song = line[4:]
      add_song()


  
  return

def pianobar(email, password):
  start_pianobar(email, password)
  choose_station()
 
  close = input('\npress ENTER to quit\n')
  SOMETHING.write('q\n')

def start_pianobar(email, password):
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  os.system('pianobar >> ' +  songs_path + 'raw.txt')
  # login
  SOMETHING.write(email)
  SOMETHING.write(password)
  return

def choose_station():
  songs_path = LIST_DIR_PATH + 'pandora_song_lists/'
  os.system('cat ' + songs_path + 'raw.txt')
  return

def quit_pianobar():
  SOMETHING.write('q')
  return

def help_them():
  return
  
def is_parse_only(argv):
  for arg in argv:
    if '-p' is arg:
      if len(argv) != 3:
        print('ERROR: wrong number of args')
      if arg is argv[1]:
        filename = argv[2]
      else:
        filename = argv[1] 
      print(" Parse Only mode on file " + filename)
      parse_output(filename)
      return 0
    return 1

def main(argv):
# check for -h option
  for arg in argv:
    if '-h' in arg:
      help_them()
      return

### Working on fixing this...
# check directory structure
#  check_dir()

### Working on fixing this...
# check for -p option (parse only)
#  is_parse_only(argv)

### Working on fixing this...
# start pianobar
#  pianobar(argv[1], argv[2])

# parse output file 
  parse_output(LIST_DIR_PATH + 'pandora_song_lists/raw.txt')

  return

if __name__ == '__main__':
  main(sys.argv)
