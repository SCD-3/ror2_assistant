from misc import menu, enums
from output import console

class SeeEnumsCommand(menu.Command):

    name = "enums"

    def run(self, *args):
        for iid, enum in enumerate(enums.ENUMS):
            console.print(f"[#ffaa00]{enum.__name__}")
            for val in enum:
                console.print(' ', f"{val.name} {' '*(22-len(val.name))}=> {val.value}", highlight=enum == enums.Rarity)
            if iid+1 != len(enums.ENUMS):
                console.print()