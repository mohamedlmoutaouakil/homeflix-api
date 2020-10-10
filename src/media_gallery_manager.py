import os
from os.path import dirname
from src.dal import add_media_list, search_by_dirname, search_by_title
import requests
from src.exceptions import NotFoundException

api_url = 'http://www.omdbapi.com/'
api_key = 'apikey'

streaming_server_url = 'http://localhost:3002/'

JSON_TO_DICT_MAPPING = {
  'actors': 'Actors', 'awards': 'Awards', 'country': 'Country', 'director': 'Directoor', 'genre': 'Genre', 
  'imdbRating': 'imdbRating', 'language': 'Language', 'mediaType': 'Type', 
  'plot': 'Plot', 'poster': 'Poster', 'rated': 'Rated', 'ratings': 'Ratings', 'released': 'Released', 
  'runtime': 'Runtime', 'title': 'Title', 'writer': 'Writer', 'year': 'Year'
}

def read_media_gellery(gallery_path):
  pass

def api_media_to_media_info(result_dict, dirname):
  media_info = dict()
  media_info['url'] = streaming_server_url + dirname
  media_info['dirname'] = dirname
  for media_info_key, result_dict_key in JSON_TO_DICT_MAPPING.items():
    if result_dict_key not in  result_dict.keys():
      media_info[media_info_key] = ''
      continue
    media_info[media_info_key] = result_dict[result_dict_key]
    if media_info_key == 'mediaType':
      if 'animation' in result_dict['Genre'].lower() and result_dict[result_dict_key] == 'series':
        media_info[media_info_key] = 'animes'
      if result_dict[result_dict_key] == 'movie':
        media_info[media_info_key] = 'movies'
  return media_info

def retrieve_info_from_api(title, dirname):
  result = requests.get(api_url + '?apikey=' + api_key + '&t=' + title)
  if not result.ok:
    raise Exception
  result_dict = result.json()
  if not result_dict['Response']:
    raise NotFoundException
  return api_media_to_media_info(result_dict, dirname)

def add_new_entries(titles_dirs_tuple_list):
  media_list = []
  for title, dirname in titles_dirs_tuple_list:
    media_info = retrieve_info_from_api(title, dirname)
    media_list.append(media_info)
  # Add media list to database
  add_media_list(media_list)

def fetch_medias(media_dir):

  media_dirs_list = list(os.walk(media_dir).__next__()[1])
  # get media title from media directory name
  titles_dirs_list = [(md.split('(')[0].strip(), md) for md in media_dirs_list]
  new_titles_dirs = list(filter(lambda tup: len(search_by_dirname(tup[1])) == 0, titles_dirs_list))
  add_new_entries(new_titles_dirs)
  return len(new_titles_dirs)