from misc.menu import Menu
from commands import *

from devmode.dev import EnableDevCommand


if __name__ == "__main__":
    
    save_file_path = None

    
    main_menu = Menu("Risk of Rain 2\nASSISTANT",
                     "Assistant to game [#C4CF4E]Risk of Rain 2",
                     #OpenItemsCommand(),
                     #ListItemsCommand(), 
                     SetCoinsCommand(),
                     SaveFileCommand(),
                     EnableDevCommand()
                     )

    main_menu.run_main()