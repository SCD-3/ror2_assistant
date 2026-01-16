from misc.const import *
from output import console

from typing import Any, Tuple, Dict, final
from pyfiglet import Figlet
from InquirerPy import inquirer
from prompt_toolkit.completion import NestedCompleter
import re as regex
import os

def clear_console():
    """
    Clear the console screen.
    """

    os.system('cls' if os.name == 'nt' else 'clear')

type Completion = dict[str, Completion]|None

class Command:
    """
    Base class for all commands.
    """

    name: str
    description: str = "PLACEHOLDER"
    description_long: str = "PLACEHOLDER"
    
    def arguments(self) -> Completion:
        return None
    
    def run(self, *args: str) -> None:
        ...


@final
class Menu:
    """
    Class representing a console menu.
    Attributes:
        title (str): The title of the menu.
        description (str): The description of the menu.
        options (tuple[Command, ...]): The available commands in the menu.
    """

    menu_stack: list["Menu"] = []
    
    def __init__(self, title: str, description: str, /, *options: Command):
        clear_console()
        
        self.small_title = title
        self.title = self.__prepare_title(title)
        self.description = description
        self.options =  options
    

    
    @property
    def options(self) -> Tuple[Command, ...]:
        return (HelpCommand(), CurrientMenuCommand()) + self.__options + (ExitCommand(),)
    @options.setter
    def options(self, val: Tuple[Command, ...]):
        self.__options = val

    @property
    def options_names(self) -> Dict[str, Command]:
        return {option.name: option for option in self.options}
    
    def __prepare_title(self, title: str) -> str:
        """Prepare the title using figlet

        Args:
            title (str): Title text

        Returns:
            str: Title ASCII art
        """

        figlet = Figlet(font="slant")
        return str(figlet.renderText(title))
    
    @staticmethod
    def __separate_arguments(t: str) -> list[str]:
        """Separate arguments in a command string.

        Args:
            t (str): Raw string to be separated.

        Returns:
            list[str]: Separated arguments.
        """

        p: list[str] = regex.findall(r'"[^"]*"|\S+', t)
        return [i.strip().lower() for i in p]
    
    def display_title(self):
        """
        Display the menu title and description.
        """

        console.print(self.title)
        console.print()
        console.print(self.description)
        console.print("Type 'help' for help")
    
    def prompt(self):
        """
        Prompt the user for a command.
        """

        console.print()
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
            raise ArgumentError(f"Invalid command: [magenta]{cmd[0]}[/]")
        try:
            self.options_names[cmd[0]].run(*cmd[1:])
        except KeyboardInterrupt:
            console.print("[magenta bold]KeyboardInterrupt[/magenta bold]")
    
    def run(self):
        """
        Run the menu loop.
        """

        clear_console()
        self.display_title()
        while True:
            res = self.prompt()
            if res:
                try:
                    self.execute(res)
                except ArgumentError as err:
                    console.print(str(err))
                except Exception as err:
                    console.print(f"[magenta bold]{err.__class__.__name__}[/magenta bold]: {err}")
    
    def run_main(self):
        """
        Run the main menu loop.
        """
        Menu.menu_stack = [self]
        self.run()
    
    def run_from(self, child: 'Menu'):
        """
        Run a child menu from the currient menu.

        Args:
            child (Menu): Menu object to be used
        """
        Menu.menu_stack.append(child)
        try:
            child.run()
        except ExitMenu:
            clear_console()
            self.display_title()
            


class MenuOpener(Command):

    child_menu: Menu
    
    def run(self, *args):
        parent_menu = Menu.menu_stack[-1]
        FLAG_RUN_AS_MAIN = False
        if len(args) >= 1:
            if args[0] == "asmain":
                FLAG_RUN_AS_MAIN = True
            else:
                raise ArgumentError("Invalid argument given. Accepts only 'asmain'.")
        
        if FLAG_RUN_AS_MAIN:
            self.child_menu.run_main()
        else:
            parent_menu.run_from(self.child_menu)
    
    def arguments(self) -> Completion:
        return {"asmain": None}


class ExitCommand(Command):
    
    name = "exit"
    description = "Exit currient menu"
    
    def arguments(self) -> Completion:
        return {'all': None}
    
    def run(self, *args):
        if len(args) >= 1:
            if args[0] == "all":
                exit()
            else:
                raise ArgumentError("Invalid argument given. Accepts only 'all'.")
        if len(Menu.menu_stack) > 1:
            Menu.menu_stack.pop()
            raise ExitMenu
        else:
            exit()
    
class HelpCommand(Command):
    
    name = "help"
    description = "Opens help menu"
    description_long = """help [<command>] - Opens help menu. If [<command>] is given, show detailed description about given command"""
    
    def __init__(self) -> None:
        self.__menu = Menu.menu_stack[-1]
    
    def arguments(self) -> Completion:
        return {i: None for i in self.__menu.options_names.keys()}
    
    def run(self, *args) -> Any:
        if len(args) == 0:
            for command in self.__menu.options:
                console.print(f"{command.name} - {command.description}")
        else:
            if args[0] not in self.__menu.options_names:
                raise ArgumentError(f"Invalid command as argument: [magenta]{args[0]}[/]")
            console.print(self.__menu.options_names[args[0]].description_long)

class CurrientMenuCommand(Command):
    
    name = "cd"
    description = "Check currient menu"
    
    def arguments(self) -> Completion:
        return {"stack": {"noname": None}, "noname": {"stack": None}}
    
    def run(self, *args: str) -> None:
        noname = "noname" in args[:2]
        stack  = "stack" in args[:2]

        if stack:
            console.print(*reversed([i if noname else i.small_title for i in Menu.menu_stack]), sep='\n'+'='*20+'\n')
        else:
            menu = Menu.menu_stack[-1]
            if noname:
                console.print(menu)
            else:
                console.print(menu.small_title)
                console.print()
                console.print(menu.description)

class ArgumentError(Exception):
    """Invalid or missing arguments for a command."""

class ExitMenu(BaseException):
    """Exit currient menu."""