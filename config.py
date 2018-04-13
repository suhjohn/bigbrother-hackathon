import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filepath = dir_path + "/name_songloc.json"
filestr = open(filepath).read()
NAME_SONG_DICT = json.loads(filestr)
