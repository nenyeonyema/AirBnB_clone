#!/usr/bin/python3
"""
Console module.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB console."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                models.storage.all().pop(key)
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        """
        args = split(line)
        if len(args) == 0:
            objects = models.storage.all()
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        else:
            objects = {k: v for k, v in models.storage.all().items()
                       if args[0] in k}
        print([str(v) for v in objects.values()])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all()[obj_key]
            setattr(obj, args[2], args[3].strip('"'))
            models.storage.save()

    def help_quit(self):
        """Help documentation for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
