import misc.enums

type Cookable = 'Item|Equipment'
type Unlockable = 'Item|Character|Skill'

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
                desc: str,
                reward: Unlockable = None,
                *,
                character: 'None|Character' = None) -> None:
        self.created.append(self)
        
        self.name = name
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
                desc: str,
                desc_long: str,
                *, 
                scaling: dict[str, tuple[int|float, misc.enums.Stacking]],
                rarity: tuple[misc.enums.Rarity, ...],
                corrupts: 'None|Item' = None,
                hardcap_at: None|int = None) -> None:
        self.created.append(self)
        
        self.name = name
        self.desc = desc
        self.desc_long = desc_long
        self.scaling = scaling
        self.rarity = rarity
        self.corrupts = corrupts
        self.hardcap_at = hardcap_at

class Equipment:
    
    created: list['Equipment'] = []
    
    def __init__(self,
                name: str,
                desc: str,
                long_desc: str,
                *,
                base_cd: int,
                lunar: bool = False,
                elite: bool = False,
                can_activate: bool = True) -> None:
        self.created.append(self)
        
        self.name = name
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
        
        self.ingredients = (item1, item2)
        self.reasult = reasult
        self.reasult_amount = reasult_amount
    
    @classmethod
    def get_from(cls, ingredient: Cookable) -> tuple['Recipe']:
        return tuple(i for i in cls.created if ingredient in i.ingredients)
    @classmethod
    def get_for(cls, reasult: Cookable) -> tuple['Recipe']:
        return tuple(i for i in cls.created if i.reasult == reasult)