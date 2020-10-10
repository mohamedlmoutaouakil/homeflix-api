import json
import os
from os.path import dirname
from src.exceptions import InvalidMediaObjectException, NotFoundException, WrongMediaTypeException

current_dir = os.getcwd()
db_path = os.path.join(current_dir, 'databases', 'medias_db.json')

with open(db_path) as f:
  medias_db = json.load(f)

media_types = ['all', 'movies', 'series', 'animes']
JSON_FIELDS = {'actors', 'awards', 'country', 'director', 'genre', 
  'imdbRating', 'language', 'mediaType', 
  'plot', 'poster', 'rated', 'ratings', 'released', 
  'runtime', 'title', 'writer', 'year', 'url', 'dirname'} # Set of the json fields in media object

def get_medias_by_type(media_type):
  if media_type not in media_types:
    raise WrongMediaTypeException
  if media_type == 'all':
    return list(medias_db['medias'].values())
  return list(filter(lambda m: m['mediaType'] == media_type, medias_db['medias'].values()))

def get_media_by_id(media_id):
  if media_id < 1 or media_id > len(medias_db['medias'].keys()):
    raise NotFoundException
  return medias_db['medias'][str(media_id)]

def search_by_title(search_str):
  return list(filter(lambda m: m['title'].lower().find(search_str.lower()) != -1, medias_db['medias'].values()))

def add_media_list(media_list):
  # check if received diect has all and valid keys 
  for media in media_list:
    if set(media.keys()) != JSON_FIELDS:
      raise InvalidMediaObjectException
  # Create database entries
  for index, media in enumerate(media_list, start=1):
    id = int(medias_db['count']) + index
    media['id'] = id # Add id to media object
    medias_db['medias'][str(id)] = media
  medias_db['count'] += len(media_list)
  with open(db_path, 'r+') as f:
    json.dump(medias_db, f)

def search_by_dirname(search_dirname):
  return list(filter(lambda m: m['dirname'] == search_dirname, medias_db['medias'].values()))