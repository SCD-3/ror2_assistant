import webbrowser

from misc.menu import Menu, Command
from output import console
from commands import *
from devmode.devstart import EnableDevCommand


class LaunchGameCommand(Command):
    
    name = 'rungame'
    description = "Run game [#C4CF4E]Risk of Rain 2"
    
    def run(self, *args):
        console.print("Launch game via a [blue]Steam[/blue]...")
        webbrowser.open(r'steam://rungameid/632360')


if __name__ == "__main__":
    
    main_menu = Menu("Risk of Rain 2\nASSISTANT",
                    "Assistant to game [#C4CF4E]Risk of Rain 2",
                    LaunchGameCommand(),
                    SetCoinsCommand(),
                    OpenConfigCommand(),
                    EnableDevCommand())

    main_menu.run_main()