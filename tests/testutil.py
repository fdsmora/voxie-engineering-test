import json
import os 

current_path = os.path.dirname(os.path.realpath(__file__)) 
json_dir = os.path.join(current_path,'json')

def load_json_from_file(file_name):
    with open(os.path.join(json_dir,file_name)) as f:
        return json.load(f)
