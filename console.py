#!/usr/bin/python3
"""
Console module.
"""

import cmd
import shlex
import argparse
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB console."""

    prompt = "(hbnb) "

    def cmdloop(self):
        while True:
            try:
                line = input(self.prompt)
                tokens = shlex.split(line)
                if tokens:
                    cmd, *args = tokens
                    if cmd == 'show':
                        self.do_show(' '.join(args))
                    elif cmd == 'create':
                        self.do_create(' '.join(args))
                    elif cmd == 'destroy':
                        self.do_destroy(' '.join(args))
                    elif cmd == 'all':
                        self.do_all(' '.join(args))
                    elif cmd == 'update':
                        self.do_update(' '.join(args))
                    else:
                        super().cmdloop(line)
            except KeyboardInterrupt:
                print("^D")
                break

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print the string representation of an
        instance based on the class name and id.
        """
        command, args, line = self.parseline(line)

        if not args:
            self.stdout.write("** class name missing **\n")
            return

        class_name = args.split()[0]
        instance_id = None

        if len(args) > 1:
            instance_id = args[1]

        if class_name not in storage.classes():
            self.stdout.write("** class doesn't exist **\n")
        elif not instance_id:
            self.stdout.write("** instance id missing **\n")
        else:
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                self.stdout.write("** no instance found **\n")
            else:
                self.stdout.write(str(storage.all()[key]) + '\n')

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            tokens = shlex.split(arg)
            class_name = tokens[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                instance_id = tokens[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """
        Print all string representations of
        instances based on the class name.
        """
        if not arg:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)
        else:
            class_name = arg
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                instances = [str(obj) for key, obj in storage.all().items()
                             if key.startswith(class_name + ".")]
                print(instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
        else:
            tokens = shlex.split(arg)
            class_name = tokens[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokens) < 2:
                print("** instance id missing **")
            else:
                instance_id = tokens[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(tokens) < 3:
                    print("** attribute name missing **")
                else:
                    attr_name = tokens[2]
                    if len(tokens) < 4:
                        print("** value missing **")
                    else:
                        value_str = tokens[3]
                        try:
                            value = eval(value_str)
                            setattr(storage.all()[key], attr_name, value)
                            storage.all()[key].save()
                        except Exception as e:
                            print(e)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty input line."""
        pass

    def help_quit(self):
        """Help documentation for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
