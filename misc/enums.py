from enum import StrEnum

class Rarity(StrEnum):

    Common = 'Common'
    Uncommon = 'Uncommon'
    Legendary = 'Legendary'
    Boss = 'Boss'
    Planet = 'Planet'
    Lunar = 'Lunar'
    Void = 'Void'
    Meal = 'Meal'
    Equipment = 'Equipment'
    Elite = 'Elite'
    Used = 'Used'

class Stacking(StrEnum):

    Linear = 'Linear'
    Hyperbolic = 'Hyperbolic'
    Reciprocal = 'Reciprocal'
    Exponential = 'Exponential'
    Special = 'Special'

class DLC(StrEnum):
    
    RiskOfRain2 = 'Risk Of Rain 2'
    SurvivorsOfTheVoid = 'Survivors of the Void'
    SeekersOfTheStorm = 'Seekers of the Storm'
    AlloyedCollective = 'Alloyed Collective'

ENUMS = (Rarity, Stacking, DLC)