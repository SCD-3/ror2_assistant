from misc.generic import params
import xml.etree.ElementTree as ET

class Achievement:
    
    #immutable
    def __init__(self, name: str, 
                 defname: str, 
                 description: str,
                 *,
                 steam_achievement: bool = True):
        self.__name = name
        self.__defname = defname
        self.__description = description
        self.__steam = steam_achievement

    @property
    def name(self):
        return self.__name
    @property
    def defname(self):
        return self.__defname
    @property
    def description(self):
        return self.__description
    @property
    def steam_achievement(self):
        return self.__steam
    
    
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
    
    

class RORobject:
    
    # immutable
    def __init__(self, name: str, defname: str, description: str, unlock: Achievement) -> None:
        self.__name = name
        self.__defname = defname
        self.__description = description
        self.__unlock = unlock
    
    @property
    def name(self):
        return self.__name
    @property
    def defname(self):
        return self.__defname
    @property
    def describiton(self):
        return self.__description