from misc.menu import Menu
from commands import *

from devmode.devstart import EnableDevCommand


if __name__ == "__main__":
    
    main_menu = Menu("Risk of Rain 2\nASSISTANT",
                    "Assistant to game [#C4CF4E]Risk of Rain 2")
    
    main_menu.options = (
        SetCoinsCommand(),
        SaveFileCommand(),
        EnableDevCommand()
        )


    main_menu.run_main()