#!/usr/bin/python3
"""This is the entry point of our program """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """custom console"""
    intro = "Our custom console, the HBNB"
    prompt = "(hbnb)"
    classes = { "BaseModel", "User", "City", "Place", "Amenity", "State", "Review"}

    def do_quit(self, line):
        """exit the console on quit command"""
        return True

    def do_EOF(self, line):
        """exit the console on CTRL+D"""
        return True

    def emptyline(self):
        """do nothing upon getting a newline"""
        pass
    def do_create(self, line):
        """ saves intances of the basemodel in the JSON file and prints it"""
        if len(line) == 0: # check if a user provide any argument
            print("** class name missing **")
        elif line not in HBNBCommand.classes: # if classname is provided but does not exist in list of classes
            print("** class doesn't  exist **")
        else:
            # if the classname exist and is provided
            bsmodel= eval(line)()
            bsmodel.save() # save to the jsonfile
            print(bsmodel.id)


    def do_show(self, line):
        """ print the string representation of the name and ID"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = tuple(line.split())
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        arg_line = parse(arg)
        objdict = storage.all()

        if len(arg_line) == 0:
            print("** class name missing **")
            return False
        if arg_line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_line) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_line[0], arg_line[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_line) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_line) == 3:
            try:
                type(eval(arg_line[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_line) == 4:
            obj = objdict["{}.{}".format(arg_line[0], arg_linel[1])]
            if arg_line[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_line[2]])
                obj.__dict__[arg_line[2]] = valtype(arg_line[3])
            else:
                obj.__dict__[arg_line[2]] = arg_line[3]
        elif type(eval(arg_line[2])) == dict:
            obj = objdict["{}.{}".format(arg_line[0], arg_line[1])]
            for k, v in eval(arg_line[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()



    def do_destroy(self,line):
        """ Deletes intances based on the class name and id and save changes to JSON file"""
        args = parse(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")









def parse(line):
    """ help parse user typed input """
    return tuple(line.split())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
