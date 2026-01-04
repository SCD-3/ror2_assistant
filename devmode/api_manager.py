from misc.menu import Command, Completion, COMMON_STYLE
from misc.const import console

import requests
import json
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator


LINK: str|None = None

class APILinkCommand(Command):
    
    name = "LinkAPI"
    description = "Control API link"
    
    def run(self, *args):
        global LINK
        try:
            act = inquirer.select(
                message="Select an action:",
                choices=[
                    Choice('set', 'Set link'),
                    Choice('read', 'See link'),
                    Choice('code', 'Get code'),
                    Separator(),
                    Choice('reset', "Remove link"),
                    Choice(None, 'Exit')
                ],
                default='read' if LINK else 'set',
                **COMMON_STYLE
            ).execute()
            
            match act:
                
                case 'set':
                    res: str = inquirer.text(message="Input API link: ", 
                                **COMMON_STYLE).execute()
                    code = requests.get(res).status_code
                    if code == 200:
                        LINK = res
                    else:
                        console.print(f"ERROR\nInvalid response\nResponse code: [yellow]{code}[/]")
                    
                
                case 'code':
                    if LINK is not None:
                        code = requests.get(LINK).status_code
                        console.print(f"[yellow]{code}[/yellow]", requests.status_codes._codes[code][0]) # pyright: ignore[reportAttributeAccessIssue]
                    else: # hey, it works so it is not my issue
                        raise ValueError("API link is not set")
            
                case 'read':
                    console.print(LINK)
                
                case 'reset':
                    proceed: bool = inquirer.confirm(message="Are you sure?", default=False, **COMMON_STYLE).execute()
                    if proceed:
                        LINK = None
                        console.print("API link has been removed.")
        except requests.ConnectionError:
            console.print("ERROR\nFailed to connect")