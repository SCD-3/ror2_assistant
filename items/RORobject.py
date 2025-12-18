from enum import StrEnum
from typing import Iterable

from misc.generic import params
import xml.etree.ElementTree as ET


class DLC(StrEnum):
    
    RoR2 = "Risk of Rain 2"
    SofV = "Survivors of the Void"
    SotS = "Seekers of the Storm"
    AC   = "Alloyed Collective"


class Achievement:
    
    def __init__(self, name: str, 
                 defname: str, 
                 description: str,
                 dlc: DLC|tuple[DLC, ...],
                 *,
                 steam_achievement: bool = True):
        
        self.name = name
        self.defname = defname
        self.description = description
        self.dlc = tuple(dlc) if isinstance(dlc, Iterable) else (dlc, )
        self.steam = steam_achievement
    
    @property
    def unlocked(self):
        if params["save_file_path"]:
            file = open(params["save_file_path"])
            tree = ET.parse(file)
            root = tree.getroot()
            
            unlock_list = root.find('achievementsList')
            if unlock_list is not None and unlock_list.text is not None:
                return self.defname in unlock_list.text
            else:
                raise ValueError("Unlocks not found")
    