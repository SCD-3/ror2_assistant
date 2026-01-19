import misc.enums

import json
import os.path

PATH = os.path.join(os.path.dirname(__file__), 'unlocks_db.json')

type rorObj = 'Ally|Artifact|Challange|Character|Environment|Interactable|Item|Equipment|Monster|Skill|Recipe'
type Cookable = 'Item|Equipment'
type Unlockable = 'Item|Character|Skill'

def save_ror_obj(obj: rorObj) -> None:
    atrs = dir(obj)
    type_name = type(obj).__name__


class Ally:
    
    created: list['Ally'] = []
    pass #TODO

class Artifact:
    
    created: list['Artifact'] = []
    pass #TODO

class Challange:
    
    created: list['Challange'] = []
    
    def __init__(self, 
                name: str, 
                defname: str,
                desc: str,
                reward: Unlockable,
                *,
                character: 'None|Character' = None) -> None:
        self.created.append(self)
        
        self.name = name
        self.defname = defname
        self.desc = desc
        self.reward = reward
        self.character = character

class Character:
    
    created: list['Character'] = []
    pass #TODO

class Environment:
    
    created: list['Environment'] = []
    
    def __init__(self,
                name: str,
                defname: str,
                title: str,
                devname: str|tuple[str],
                *,
                stage: int,
                lore: str,
                monsters: 'tuple[Monster]',
                family_events: 'tuple[Monster]',
                interactables: 'tuple[Interactable]'
                ) -> None:
        self.created.append(self)
        
        self.name = name
        self.defname = defname
        self.title = title
        self.devname = devname
        self.stage = stage
        self.lore = lore
        self.monsters = monsters
        self.family_events = family_events
        self.interactables = interactables

class Interactable:
    
    created: list['Interactable'] = []
    pass #TODO

class Item:
    
    created: list['Item'] = []

    def __init__(self,
                name: str,
                defname: str,
                desc: str,
                desc_long: str,
                *, 
                scaling: dict[str, tuple[int|float, misc.enums.Stacking]],
                rarity: tuple[misc.enums.Rarity, ...],
                corrupts: 'None|Item|misc.enums.Rarity' = None,
                hardcap_at: None|int = None,
                oneuse: bool = False,
                turns_into: None|Item = None) -> None:
        self.created.append(self)
        
        self.name = name
        self.defname = defname
        self.desc = desc
        self.desc_long = desc_long
        self.scaling = scaling
        self.rarity = rarity
        self.corrupts = corrupts
        self.hardcap_at = hardcap_at
        self.oneuse = oneuse
        self.turns_into = turns_into

class Equipment:
    
    created: list['Equipment'] = []
    
    def __init__(self,
                name: str,
                defname: str,
                desc: str,
                long_desc: str,
                *,
                base_cd: int,
                lunar: bool = False,
                elite: bool = False,
                can_activate: bool = True) -> None:
        self.created.append(self)
        
        self.name = name
        self.defname = defname
        self.desc = desc
        self.long_desc = long_desc
        self.base_cd = base_cd
        self.rarity = ((misc.enums.Rarity.Lunar,) if lunar else ()) + (misc.enums.Rarity.Equipment,) + ((misc.enums.Rarity.Elite,) if elite else ())
        self.can_activate = can_activate

class Monster:
    
    created: list['Monster'] = []
    pass #TODO

class Skill:
    
    created: list['Skill'] = []
    
    def __init__(self, 
                name: str,
                desc: str,
                long_desc: str,
                *,
                character: 'Character',
                base_cd: int,
                charges: int = 1,
                slot: misc.enums.SkillSlot,
                proc: float = 1.0) -> None:
        self.created.append(self)
        
        self.name = name
        self.defname = name.replace(' ', '_')
        self.desc = desc
        self.long_desc = long_desc
        self.character = character
        self.base_cd = base_cd
        self.charges = charges
        self.slot = slot
        self.proc = proc

class Recipe:
    
    created: list['Recipe'] = []
    
    def __init__(self,
                item1:   Cookable,
                item2:   Cookable,
                reasult: Cookable,
                *,
                reasult_amount: int = 1) -> None:
        self.created.append(self)
        
        self.defname = f"{item1.defname}_AND_{item2.defname}_TO_{reasult.defname}"
        self.ingredients = (item1, item2)
        self.reasult = reasult
        self.reasult_amount = reasult_amount
    
    @classmethod
    def get_from(cls, ingredient: Cookable) -> tuple['Recipe', ...]:
        return tuple(i for i in cls.created if ingredient in i.ingredients)
    @classmethod
    def get_for(cls, reasult: Cookable) -> tuple['Recipe', ...]:
        return tuple(i for i in cls.created if i.reasult == reasult)