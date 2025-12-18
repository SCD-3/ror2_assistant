from misc.menu import Command, ArgumentError, Completion
from items.artifacts.artifacts_checklist import LIST_OF_ARTIFACTS

class OpenItemsCommand(Command):
    
    name = "open"
    description = "Open artifact details. Takes artifact name as argument."
    
    def _arguments(self) -> Completion:
        return {'artifact': {i: None for i in LIST_OF_ARTIFACTS},
                'item': None,
                'equipment': None,
                'character': None,
                'enemy': None,
                'environment': None,
                'unlock': None
                }
        
    
    def run(self, *args) -> None:
        
        if len(args) < 1 or args[0] not in self.arguments:
            raise ArgumentError("Please provide a valid object name as argument.")
        




class ListItemsCommand(Command):
    
    name = "list"
    description = "List all objects."
    
    def _arguments(self) -> Completion:
        return {'artifact': None,
                'item': None,
                'equipment': None,
                'character': None,
                'enemy': None,
                'environment': None,
                'unlock': None,
                'all': None
                }
    
    def run(self, *args) -> None:
        print("Available Artifacts:")
        for artifact in LIST_OF_ARTIFACTS.values():
            status = "\033[32m✓\033[0m" if artifact.unlocked else "\033[31m✗\033[0m"
            print(f"- {artifact.full_name.ljust(30)} {status}")