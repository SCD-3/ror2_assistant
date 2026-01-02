from typing import Any, Literal
from pyfiglet import Figlet
from InquirerPy import inquirer
from rich import print as rprint
from prompt_toolkit.completion import NestedCompleter
import re as regex
import os

def clear_console():
    """
    Clear the console screen.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

type Completion = dict[str, Completion|None]|None

COMMON_STYLE: dict[Literal['qmark', 'amark'], str]
COMMON_STYLE = {'qmark': '>', 'amark': '>'}

class Command:
    """
    Base class for all commands.
    """

    name: str
    description: str = "PLACEHOLDER"
    description_long: str = "PLACEHOLDER"
    
    def arguments(self) -> Completion:
        return None
    
    def run(self, *args) -> Any:
        ...



class Menu:
    """
    Class representing a console menu.
    Attributes:
        title (str): The title of the menu.
        description (str): The description of the menu.
        options (tuple[Command, ...]): The available commands in the menu.
    """

    def __init__(self, title: str, description: str, /, *options: Command):
        clear_console()
        
        self.title = self.__prepare_title(title)
        self.description = description
        self.__help = HelpCommand(self)
        self.__exit = ExitCommand()
        self.options =  options

    
    @property
    def options(self):
        return (self.__help,) + self.__options + (self.__exit,)
    @options.setter
    def options(self, val):
        self.__options = val

    @property
    def options_names(self):
        return {option.name: option for option in self.options}
    
    def __prepare_title(self, title: str) -> str:
        """
        Prepare the title using figlet.
        """

        figlet = Figlet(font="slant")
        return figlet.renderText(title)
    
    @staticmethod
    def __separate_arguments(t: str):
        """
        Separate arguments in a command string.
        """

        p: list[str] = regex.findall(r'"[^"]*"|\S+', t)
        return [i.strip() for i in p]
    
    def display_title(self):
        """
        Display the menu title and description.
        """

        print(self.title)
        print()
        print(self.description)
        rprint("Type '[yellow]help[/yellow]' for help")
    
    def prompt(self):
        """
        Prompt the user for a command.
        """

        print()
        res: str = inquirer.text(message="", 
                            completer=NestedCompleter.from_nested_dict({cmd.name: cmd.arguments() for cmd in self.options}),
                            **COMMON_STYLE).execute()
        res_args = Menu.__separate_arguments(res)
        return res_args

    def execute(self, cmd: list[str]):
        """
        Execute a command.
        """

        if cmd[0] not in self.options_names:
            raise ArgumentError(f"Invalid command: {cmd[0]}")
        self.options_names[cmd[0]].run(*cmd[1:])
    
    def run(self):
        """
        Run the menu loop.
        """

        clear_console()
        self.display_title()
        while True:
            res = self.prompt()
            try:
                self.execute(res)
            except ArgumentError as err:
                print(err)
            except Exception as err:
                print(f"{err.__class__.__name__}: {err}")
    
    def run_main(self):
        """
        Run the main menu loop.
        """
        try:
            self.run()
        except ExitMenu:
            exit(1)
    
    def run_from(self, child: 'Menu'):
        """
        Run a child menu from the current menu.
        """
        try:
            child.run()
        except ExitMenu:
            clear_console()
            self.display_title()


class ExitCommand(Command):
    
    name = "exit"
    description = "Exit the application"
    
    def run(self, *args):
        raise ExitMenu
    
class HelpCommand(Command):
    
    name = "help"
    description = "Opens help menu"
    description_long = """help [<command>] - Opens help menu. If [<command>] is given, show detailed description about given command"""
    
    def __init__(self, menu: Menu) -> None:
        self.__menu = menu
    
    def arguments(self):
        return {i: None for i in self.__menu.options_names.keys()}
    
    def run(self, *args) -> Any:
        if len(args) == 0:
            for command in self.__menu.options:
                print(f"{command.name} - {command.description}")
        else:
            if args[0] not in self.__menu.options_names:
                raise ArgumentError(f"Invalid command as argument: {args[0]}")
            print(self.__menu.options_names[args[0]].description_long)


class ArgumentError(Exception):
    """Invalid or missing arguments for a command."""

class ExitMenu(BaseException):
    """Exit currient menu."""