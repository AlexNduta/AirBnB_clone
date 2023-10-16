#!/usr/bin/python3
"""storage of file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}
    class_dict = {
            "BaseModel": BaseModel
            }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
            obj_dict[key]["__class__"] = obj.__class__.name__


        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name:
                        del value["__class__"]
                        instance = self.class_dict[cls_name](**value)
                        key = "{}.{}".format(cls_name, instance.id)
                        FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass


storage = FileStorage()
