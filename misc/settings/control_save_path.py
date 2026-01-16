import json
import os.path
import xml.etree.ElementTree as ET
import re as regex
from typing import Any
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import PathValidator

import misc.const
from misc.menu import Command


EMPTY_CONFIG = {
    "profile_path": "",
    "selected_profile": ""
}

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
if not os.path.exists(CONFIG_PATH):
    json.dump(EMPTY_CONFIG, open(CONFIG_PATH, 'w'))
JSON_DATA = json.load(open(CONFIG_PATH))

def get_confing():
    return json.load(open(CONFIG_PATH))

def _update_config_file(j: Any):
    json.dump(j, open(CONFIG_PATH, 'w'))

def _get_profiles():
    all_profiles: list[str] = os.listdir(JSON_DATA['profile_path'])
    all_profiles.remove('config.cfg')
    return all_profiles

class SetProfilePathCommand(Command):
    
    name = "setprofile"
    description = "Open menu for save file path managment"
    
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
            default='read' if JSON_DATA['profile_path'] else 'set',
            **misc.const.COMMON_STYLE
        ).execute()
        
        match act:
            
            case 'set':
                home_path = "~/" if os.name == "posix" else "C:\\"
                new_path = inquirer.filepath(
                            message="Enter your profile folder path:",
                            default=home_path,
                            validate=PathValidator(is_dir=True, message="Input is not a directory"),
                            **misc.const.COMMON_STYLE
                            ).execute()
                JSON_DATA['profile_path'] = new_path
        
            case 'read':
                misc.const.console.print(JSON_DATA['profile_path'])
            
            case 'reset':
                proceed: bool = inquirer.confirm(message="Are you sure?", default=False, **misc.const.COMMON_STYLE).execute()
                if proceed:
                    JSON_DATA['profile_path'] = ""
                    misc.const.console.print("Save file path has been removed.")
        
        _update_config_file(JSON_DATA)


class ChangeProfileCommand(Command):
    
    name = "switchprofile"
    description = "Switch curriently active profile"
    
    def run(self, *args: str) -> None:
        def get_name(i: str):
            tree = ET.parse(i)
            root = tree.getroot()
            name = root.find('name')
            if name is not None and name.text is not None:
                return name.text
            else:
                raise ValueError(f'Name not found in profile {i}')
        
        profile = inquirer.select(
            message="Select a profile:",
            choices=[Choice((i, _:=get_name(os.path.join(JSON_DATA['profile_path'], i))), _.ljust(10)+i[:-4]) for i in _get_profiles()],
            transformer=lambda a: (regex.findall(r'^(.+) ', a[::-1])[0])[::-1].strip(),
            **misc.const.COMMON_STYLE).execute()
        
        misc.const.console.print(f"Profile has been changed to [blue]{profile[1]}")
        JSON_DATA['selected_profile'] = profile[0]
        
        _update_config_file(JSON_DATA)