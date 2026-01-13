from misc import menu, const, enums

class SeeEnumsCommand(menu.Command):

    name = "enums"

    def run(self, *args):
        for iid, enum in enumerate(enums.ENUMS):
            const.console.print(f"[#ffaa00]{enum.__name__}")
            for val in enum:
                const.console.print(' ', val.name)
            if iid+1 != len(enums.ENUMS):
                const.console.print()