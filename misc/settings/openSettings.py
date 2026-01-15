from misc.menu import MenuOpener, Menu
from misc.settings.control_save_path import SetProfilePathCommand, ChangeProfileCommand

settings_menu = Menu(
    "Settings",
    "Configuration and settings for [#C4CF4E]Risk of Rain 2 Assistant",
    SetProfilePathCommand(),
    ChangeProfileCommand()
)


class OpenConfigCommand(MenuOpener):
    name = 'config'
    description = "Opens configuration panel."
    
    child_menu = settings_menu