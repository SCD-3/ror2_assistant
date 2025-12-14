from typing import Literal
from misc.menu import Menu, Command, ArgumentError

params: dict[Literal['save_file_path'], str|None]
params = {
    "save_file_path": None
}

class ExitCommand(Command):
    
    name = "exit"
    description = "Exit the application"
    
    def __call__(self, *args):
        exit(0)

class SaveFilePathCommand(Command):
    
    name = "savepath"
    description = "Set the save file path."
    
    def __call__(self, *args):
        if len(args) == 0 or not isinstance(args[0], str):
            print(params["save_file_path"])
        else:
            params["save_file_path"] = args[0]