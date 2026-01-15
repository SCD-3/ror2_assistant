class Ally:
    pass #TODO

class Artifact:
    pass #TODO

class Challange:
    
    def __init__(self, 
                name: str, 
                describtion: str,
                reward: None|Item|Character|Skill = None,
                *,
                character: None|Character = None) -> None:
        pass #TODO

class Character:
    pass #TODO

class Environment:
    
    def __init__(self,
                name: str,
                title: str,
                devname: str|tuple[str],
                *,
                stage: int,
                lore: str,
                monsters: tuple[Monster],
                family_events: tuple[Monster],
                interactables: tuple[Interactable]
                ) -> None:
        
        self.name = name
        self.title = title
        self.devname = devname
        self.stage = stage
        self.lore = lore
        self.monsters = monsters
        self.family_events = family_events
        self.interactables = interactables

class Interactable:
    pass #TODO

import misc.enums

class Item:

    def __init__(self,
                name: str,
                desc: str,
                desc_long: str,
                *, 
                scaling: dict[str, tuple[int|float, misc.enums.Stacking]],
                rarity: tuple[misc.enums.Rarity, ...],
                corrupts: 'None|Item' = None,
                hardcap_at: None|int = None) -> None:
        
        self.name = name
        self.desc = desc
        self.desc_long = desc_long
        self.scaling = scaling
        self.rarity = rarity
        self.corrupts = corrupts
        self.hardcap_at = hardcap_at

class Monster:
    pass #TODO

class Skill:
    pass #TODO