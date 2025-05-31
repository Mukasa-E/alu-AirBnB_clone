#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    class_map = {
        'BaseModel': BaseModel
    }

    def all(self, cls=None):
      if  cls is not None and not isinstance(cls, type):
         raise TypeError("cls must be a class")
      if  cls is None:
         return self.__objects
      return {
        key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)
    }

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value.get('__class__')
                    cls = self.class_map.get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
