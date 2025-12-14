from typing import Any
from misc.generic import ExitCommand, SaveFilePathCommand
from misc.menu import Menu, Command
from artifacts.artifacts_checklist import OpenArtifactCommand, ListArtifactsCommand
from lunar_coin_control import SetCoinsCommand

# "C:\Program Files (x86)\Steam\userdata\851411552\632360\remote\UserProfiles\fddada63-5096-4d0d-8e6d-885d98884467.xml"

if __name__ == "__main__":
    
    save_file_path = None

    
    main_menu = Menu("Risk of Rain 2\nASSISTANT+",
                     ExitCommand,
                     OpenArtifactCommand,
                     ListArtifactsCommand, 
                     SetCoinsCommand,
                     SaveFilePathCommand,
                     description="Assistant to game Risk of Rain 2\nType 'help' for help")

    main_menu.run()