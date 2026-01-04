from misc.menu import Command, Completion, Menu
from devmode.devmenu import dev_menu

class EnableDevCommand(Command):
    name = "devmode"
    description = "Open developer mode for advanced control."

    def __init__(self, menu: Menu) -> None:
        self.menu = menu
    
    def run(self, *args):
        FLAG_RUN_AS_MAIN = len(args) >= 1 and args[0] == "asmain"
        
        if FLAG_RUN_AS_MAIN:
            dev_menu.run_main()
        else:
            self.menu.run_from(dev_menu)
    
    def arguments(self) -> Completion:
        return {"asmain": None}