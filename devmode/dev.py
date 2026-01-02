from misc.menu import Command, COMMON_STYLE

import hashlib
import os.path
from InquirerPy import inquirer
from rich.console import Console

def __create_defult_password():
    path = os.path.join(os.path.dirname(__file__), "devpass")
    with open(path, 'wb') as file:
        file.write(hashlib.md5('password'.encode()))

class EnableDevCommand(Command):
    name = "devmode"
    description = "Open developer mode for advanced control."

    @staticmethod
    def __read_password():
        path = os.path.join(os.path.dirname(__file__), "devpass")
        with open(path, 'rb') as file:
            return file.read()

    def run(self, *args):
        console_password = Console(force_terminal=True, color_system='truecolor').render_str
        password_match = lambda a: self.__read_password() == hashlib.md5(a.encode())

        inquirer.secret(
            message="Enter password to access devmode:",
            transformer=lambda p: console_password("\[[green]Access Granted[/green]]" if password_match(p) else "\[[red]Access Rejected[/red]]"),
            **COMMON_STYLE
        )