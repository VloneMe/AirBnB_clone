#!/usr/bin/python3

"""Module contains the entry point of the command interpreter"""

import cmd
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand command interpretor class
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """The exit method of the command"""
        return True

    def help_quit(self):
        """
        Display help for the quit command.
        """
        print("Quit command to exit the program")
        print("Usage: quit")

    def do_EOF(self, arg):
        """The exit method with Ctrl-D"""
        return True

    def help_EOF(self):
        """
        Display help for the exit command.
        """
        print("EOF - End-Of-File command to stop interpreter.")
        print("Usage: EOF")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it to JSON, and print its ID.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            new_inst = eval(class_name)()
            new_inst.save()
            print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print string representation of an instance based on class name and ID.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and ID.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances.
        """
        args = arg.split()

        if len(args) == 0:
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
        elif args[0] in self.classes():
            all_objs = storage.all()
            filtered_objects = {
                key: obj for key, obj in all_objs.items()
                if obj.__class__.__name__ == args[0]
            }
            for obj in filtered_objects.values():
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on class name, ID, attribute name, and value.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key in all_objs:
            obj = all_objs[key]

            if len(args) < 3:
                print("** attribute name missing **")
                return

            if len(args) < 4:
                print("** value missing **")
                return

            attr_name = args[2]
            attr_value = " ".join(args[3:])
            attr_value = attr_value.strip('"')

            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** no instance found **")

    def classes(self):
        """
        Returns a dictionary of available classes.
        """
        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return classes_dict

    def storage(self):
        """
        Returns the storage instance.
        """
        return storage()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
