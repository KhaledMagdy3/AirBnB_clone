#!/usr/bin/python3
"""Console module."""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter class."""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def help_quit(self.arg):
        """help_quit"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
