from misc.menu import MenuOpener, Menu
from devmode.dev_commands import *


dev_menu = Menu("DEVMODE",
                "Developer menu for advanced functionality",
                APILinkCommand())

class EnableDevCommand(MenuOpener):
    name = "devmode"
    description = "Open developer mode for advanced control."
    target_menu = dev_menu