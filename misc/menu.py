from typing import Any, Iterable, Optional
from pyfiglet import Figlet
from InquirerPy import inquirer, get_style
from prompt_toolkit.completion import NestedCompleter
import re as regex
import os

def clear_console():
    # return
    os.system('cls' if os.name == 'nt' else 'clear')

type Completion = dict[str, Completion|None]

class Command:
    
    name: str = ""
    description: str = ""
    description_long: str = ""
    
    def __init__(self, *args, **kwargs) -> None:
        self.arguments: Completion = {self.name: None}
    
    def __call__(self, *args) -> Any:
        pass



class Menu:
    
    def __init__(self, title: str, *options: Command, description: str = ""):
        clear_console()
        
        self.title = self.__prepare_title(title)
        self.options = options + (help_cmd := HelpCommand(self),)
        self.options_names = {option.name: option for option in self.options}
        # print(self.options_names)
        help_cmd.add_arguments()
        self.description = description
        
    def __prepare_title(self, title: str) -> str:
        figlet = Figlet(font="slant")
        return figlet.renderText(title)
    
    @staticmethod
    def __separate_arguments(t: str):
        p: list[str] = regex.findall(r'"[^"]*"|\S+', t)
        return [i.strip() for i in p]
    
    def display_title(self):
        print(self.title)
        print()
        if self.description:
            print(self.description)
            print()
    
    def prompt(self):
        res: str = inquirer.text(message="",
                            # completer={cmd.name: cmd.arguments for cmd in self.options}).execute()
                            completer=NestedCompleter.from_nested_dict({cmd.name: cmd.arguments for cmd in self.options}),
                            qmark='>', amark='>').execute()
        res_args = Menu.__separate_arguments(res)
        self.options_names[res_args[0]](*res_args[1:])

    def run(self):
        clear_console()
        self.display_title()
        while True:
            self.prompt()
    
    
class HelpCommand(Command):
    
    name = "help"
    description = "Opens help menu"
    description_long = """help [<command>] - Opens help menu. If [<command>] is given, show detailed description about given command"""
    
    def __init__(self, menu: Menu) -> None:
        self.__menu = menu
    
    def add_arguments(self):
        self.arguments = {i: None for i in self.__menu.options_names.keys()}
    
    def __call__(self, *args) -> Any:
        if len(args) == 0:
            for command in self.__menu.options:
                print(f"{command.name} - {command.description}")
        else:
            print(self.__menu.options_names[args[0]].description_long)



class ArgumentError(Exception):
    """Invalid or missing arguments for a command."""