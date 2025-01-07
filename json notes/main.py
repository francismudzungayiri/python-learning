import json
import os



with open(os.path.expanduser("/Users/mbuluundi/Desktop/python/json notes/o1_names.json"), 'r') as names_data:
    data =json.load(names_data)
    print(data)