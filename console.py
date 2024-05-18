#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + enter does not execute"""
        pass

    def do_quit(self, arg):
        """quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
