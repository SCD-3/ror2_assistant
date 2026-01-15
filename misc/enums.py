from enum import StrEnum, auto

def _auto(name: str):
    return name.replace('_', ' ')

class Rarity(StrEnum):

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return _auto(name)

    Common = auto()
    Uncommon = auto()
    Legendary = auto()
    Boss = auto()
    Planet = auto()
    Lunar = auto()
    Void = auto()
    Meal = auto()
    Equipment = auto()
    Elite = auto()
    Used = auto()


class Stacking(StrEnum):

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return _auto(name)

    Linear = auto()
    Hyperbolic = auto()
    Reciprocal = auto()
    Exponential = auto()
    Special = auto()


class DLC(StrEnum):

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
        return _auto(name)

    Risk_Of_Rain_2 = auto()
    Survivors_Of_The_Void = auto()
    Seekers_Of_The_Storm = auto()
    Alloyed_Collective = auto()


ENUMS = (Rarity, Stacking, DLC)