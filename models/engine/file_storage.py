#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage():
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        n_dict = {}
        for key, value in FileStorage.__objects.items():
            n_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(n_dict, my_file)
    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
     
