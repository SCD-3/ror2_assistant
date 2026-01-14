import unlocks.items
import unlocks.characters
import unlocks.skills

class Challange:
    
    def __init__(self, 
                name: str, 
                describtion: str,
                reward: None|unlocks.items.Item|unlocks.characters.Character|unlocks.skills.Skill = None,
                *,
                character: None|unlocks.characters.Character = None) -> None:
        pass #TODO