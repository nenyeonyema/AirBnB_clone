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
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def help_quit(self):
        """Help documentation for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help documentation for EOF command."""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
