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
import argparse

LIST_DIR_PATH = "/home/jho/code/py/pan_list/"
songs_path = LIST_DIR_PATH + 'pandora_song_lists/raw.txt'

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
  f = open(songs_path + station, 'w')
  f.write('This is a list of all songs played on Pandora station ' + station)
  f.close()
  return

def check_file():
  command = "ls " + songs_path + " | grep ' " + station + " '"
  if not os.system(command):
    return 0
  else:
    new_file()
    return

def add_song():
  if check_songs():
    return
  f = open(songs_path + station, 'a')
  f.write(song)
  f.close()
  return

def check_songs():
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

def main(argv):
# check args (-h) help (-e) email (-p) passwd (-o) parse only
  parser = argparse.ArgumentParser(description='Complete, organized song history for pianobar/Pandora')
  parser.add_argument('-e', '--email', default='none', nargs='?', metavar='EMAIL', type=str, help='Pandora Username')
  parser.add_argument('-p', '--passwd', default='none', nargs='?', metavar='PASS', type=str, help='Pandora Password')
  parser.add_argument('-o', '--parse_only', action='count', help='Parse an existing file')
  parser.add_argument('-f', '--filename', default=songs_path+'raw.txt', metavar='FILE', type=int, help='Alternate file to be used instead of pandora_song_lists/raw.txt')
  args = parser.parse_args()
  if args.parse_only:
    print(" Parse Only mode on file " + args.filename)
    parse_output(filename)
    return

### Working on fixing this...
# check directory structure
#  check_dir()

### Working on fixing this...
# start pianobar
#  pianobar(email, passwd)

# parse output file 
  parse_output(args.filename)

  return

if __name__ == '__main__':
  main(sys.argv)
