from typing import Any, Callable, Type
from pyfiglet import Figlet
from InquirerPy import inquirer
import re as regex
import os
import builtins

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



class Menu:
    
    def __init__(self, title: str, *options: Type["Command"], description: str = ""):
        clear_console()
        
        self.title = self.__prepare_title(title)
        self.options = options
        self.options_names = {option.name: option for option in options}
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
                            completer={cmd: None for cmd in self.options_names}).execute()
        res_args = Menu.__separate_arguments(res)
        self.options_names[res_args[0]]()(*res_args[1:])

    def run(self):
        clear_console()
        self.display_title()
        while True:
            self.prompt()



class Command:
    
    name: str = ""
    description: str = ""
    description_long: str = ""
    
    def __call__(self, *args) -> Any:
        pass

class ArgumentError(Exception):
    """Invalid or missing arguments for a command."""


if __name__ == "__main__":
    print(input(lambda cmd: True))