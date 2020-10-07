import json
import os
from src.exceptions import NotFoundException, WrongMediaTypeException

current_dir = os.getcwd()
db_path = os.path.join(current_dir, 'databases', 'medias_db.json')

with open(db_path) as f:
  medias_db = json.load(f)

media_types = ['all', 'movies', 'series', 'animes']

def get_medias_by_type(media_type):
  if media_type not in media_types:
    raise WrongMediaTypeException
  if media_type == 'all':
    return medias_db['medias']
  return list(filter(lambda m: m['mediaType'] == media_type, medias_db['medias'].values()))

def get_media_by_id(media_id):
  if media_id < 1 or media_id > len(medias_db['medias'].keys()):
    raise NotFoundException
  return medias_db['medias'][str(media_id)]

def search_by_title(search_str):
  return list(filter(lambda m: m['title'].lower().find(search_str.lower()) != -1, medias_db['medias'].values()))