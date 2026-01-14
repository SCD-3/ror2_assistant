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
