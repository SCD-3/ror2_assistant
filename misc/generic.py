from typing import Literal
from misc.menu import Command
from misc.const import *

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import PathValidator

import os
import xml.etree.ElementTree as ET


class SaveFile:

    def __init__(self, path: str|None = None):
        self.update_path(path)
    
    def update_path(self, new_path: str|None = None):
        if new_path is not None:
            self.path = new_path
            self.file = open(self.path)
            self.xml  = ET.parse(self.file)
            self.root = self.xml.getroot()
        else:
            self.path = None
            self.file = None
            self.xml  = None
            self.root = None
    
    @property
    def exists(self):
        if self.path is None:
            return False
        else:
            return os.path.exists(self.path)
    
    def __bool__(self):
        return self.exists
    
    def __str__(self):
        return self.path

SAVEPATH = SaveFile()

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
            default='read' if SAVEPATH else 'set',
            **COMMON_STYLE
        ).execute()
        
        match act:
            
            case 'set':
                home_path = "~/" if os.name == "posix" else "C:\\"
                new_path = inquirer.filepath(
                            message="Enter your savefile:",
                            default=home_path,
                            validate=PathValidator(is_file=True, message="Input is not a file"),
                            **COMMON_STYLE
                            ).execute()
                SAVEPATH.update_path(new_path)
        
            case 'read':
                console.print(SAVEPATH)
            
            case 'reset':
                proceed = inquirer.confirm(message="Are you sure?", default=False, **COMMON_STYLE).execute() # type: ignore
                if proceed:
                    SAVEPATH.update_path()
                    console.print("Save file path has been removed.")