from src.dal import get_media_by_id, get_medias_by_type, search_by_title
from src.exceptions import NotFoundException, WrongMediaTypeException

def media_by_id(media_id):
  try:
    media = get_media_by_id(media_id)
  except NotFoundException as e:
    return 'Media Not Found', 404
  except Exception as e:
    return 'Internal server error', 500
  return media, 200

def medias_by_type(media_type):
  try:
    medias_list = get_medias_by_type(media_type)
  except WrongMediaTypeException as e:
    return 'Requested Wrong Media Type', 400 
  except Exception as e:
    return 'Internal server error', 500
  return medias_list, 200

def search(title):
  try:
    media_list = search_by_title(title)
  except Exception as e:
    return 'Internal server error', 500
  return media_list, 200