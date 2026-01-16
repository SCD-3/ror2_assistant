import misc.enums

type Cookable = 'Item|Equipment'

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

class Equipment:
    
    def __init__(self,
                name: str,
                desc: str,
                long_desc: str,
                *,
                base_cd: int,
                lunar: bool = False,
                elite: bool = False,
                can_activate: bool = True) -> None:
        
        self.name = name
        self.desc = desc
        self.long_desc = long_desc
        self.base_cd = base_cd
        self.rarity = ((misc.enums.Rarity.Lunar,) if lunar else ()) + (misc.enums.Rarity.Equipment,) + ((misc.enums.Rarity.Elite,) if elite else ())
        self.can_activate = can_activate

class Monster:
    pass #TODO

class Skill:
    pass #TODO

class Recipe:
    
    def __init__(self,
                item1:   Cookable,
                item2:   Cookable,
                reasult: Cookable,
                *,
                reasult_amount: int = 1) -> None:
        
        self.ingredients = (item1, item2)
        self.reasult = reasult
        self.reasult_amount = reasult_amount