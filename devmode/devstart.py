from output import console
from misc.menu import MenuOpener, Menu, Command
from devmode.dev_commands import *

class PrintCommand(Command):
    name = "print"
    description = "Print a message to the console."
    
    def run(self, *args):
        message = " ".join(args)
        console.print(message)

dev_menu = Menu("DEVMODE",
                "Developer menu for advanced functionality",
                PrintCommand(),
                SeeEnumsCommand())

class EnableDevCommand(MenuOpener):
    name = "devmode"
    description = "Open developer mode for advanced control."
    child_menu = dev_menu