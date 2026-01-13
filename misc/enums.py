from enum import Flag, auto

class Rarity(Flag):

    Common = auto()
    Uncommon = auto()
    Legendary = auto()
    Boss = auto()
    Lunar = auto()
    Void = auto()
    Meal = auto()
    Equipment = auto()
    Elite = auto()

class Stacking(Flag):

    Linear = auto()
    Hyperbolic = auto()
    Reciprocal = auto()
    Exponential = auto()
    Special = auto()