from misc.menu import Command

class EnableDevCommand(Command):
    name = "devmode"
    description = "Open developer mode for advanced control."

    def run(self, *args):
        raise NotImplementedError