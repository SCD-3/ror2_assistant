from typing import Literal
from misc.menu import Command
from misc.const import *

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import PathValidator

import os

params: dict[Literal['save_file_path'], str|None]
params = {
    "save_file_path": None
}

class SaveFileCommand(Command):
    
    name = "savepath"
    description = "Open menu for save file managment"
    
    def run(self, *args):
        act = inquirer.select(
            message="Select an action:",
            choices=[
                Choice('set', 'Set path'),
                Choice('read', 'See path'),
                Separator(),
                Choice('reset', "Remove path"),
                Choice(None, 'Exit')
            ],
            default='read' if params["save_file_path"] else 'set',
            **COMMON_STYLE
        ).execute()
        
        match act:
            
            case 'set':
                home_path = "~/" if os.name == "posix" else "C:\\"
                params["save_file_path"] = inquirer.filepath(
                            message="Enter your savefile:",
                            default=home_path,
                            validate=PathValidator(is_file=True, message="Input is not a file"),
                            **COMMON_STYLE
                            ).execute()
        
            case 'read':
                console.print(params["save_file_path"])
            
            case 'reset':
                proceed = inquirer.confirm(message="Are you sure?", default=False, **COMMON_STYLE).execute() # type: ignore
                if proceed:
                    params["save_file_path"] = None
                    console.print("Save file path has been removed.")