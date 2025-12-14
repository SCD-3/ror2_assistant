from typing import Any, Callable, Type
from pyfiglet import Figlet
import InquirerPy as inquirer
import re as regex
import os
import builtins

def input(validator: Callable[[tuple[str, ...]], bool]) -> tuple[str, ...]:
    while True:
        user_input = builtins.input("> ")
        user_input = tuple(regex.findall(r'"[^"]*"|\S+', user_input))
        user_input = tuple(i.strip('"') for i in user_input)
        if validator(user_input):
            return user_input
        else:
            print(f"Invalid command: {user_input[0]}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



class Menu:
    
    def __init__(self, title: str, *options: Type["Command"], description: str = ""):
        clear_console()
        
        self.title = self.__prepare_title(title)
        self.options = options
        self.__options_names = {option.name: option for option in options}
        self.description = description
        
    def __prepare_title(self, title: str) -> str:
        figlet = Figlet(font="slant")
        return figlet.renderText(title)
    
    def display(self, show_title: bool = False):
        if show_title:
            print(self.title)
            print()
            if self.description:
                print(self.description)
                
        print()
        for option in self.options:
            print(f"{option.name}: {option.description}")
    
    def prompt(self):
        res = input(lambda cmd: cmd[0] in self.__options_names)
        self.__options_names[res[0]]()(*res[1:])

    def run(self):
        show_title = True
        clear_console()
        while True:
            self.display(show_title)
            show_title = False
            self.prompt()



class Command:
    
    name: str
    description: str
    
    def __call__(self, *args) -> Any:
        pass

class ArgumentError(Exception):
    """Invalid or missing arguments for a command."""


if __name__ == "__main__":
    print(input(lambda cmd: True))