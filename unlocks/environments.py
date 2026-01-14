import unlocks.monsters
import unlocks.interactables

from typing import Iterable

class Environment:
    
    def __init__(self,
                name: str,
                title: str,
                devname: str|Iterable[str],
                *,
                stage: int,
                lore: str,
                monsters: Iterable[unlocks.monsters.Monster],
                family_events: Iterable[unlocks.monsters.Monster],
                interactables: Iterable[unlocks.interactables.Interactable]
                ) -> None:
        
        self.name = name
        self.title = title
        self.devname = devname
        self.stage = stage
        self.lore = lore
        self.monsters = monsters
        self.family_events = family_events
        self.interactables = interactables