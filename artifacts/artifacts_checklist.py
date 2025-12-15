import json
import os.path
from typing import final
import re as regex

from misc.menu import Command, ArgumentError, Completion
from misc.generic import params

@final
class Artifact:

    MATTER = '■'
    DESIGN = '●'
    BLOOD  = '▲'
    SOUL   = '◆'
    
    # Artifacts is immutable
    def __init__(self, name: str, /) -> None:
        fdir = os.path.dirname(__file__)
        self.__data = json.load(open(os.path.join(fdir, 'artifacts.json')))[name]
        
        self.__id: str          = name
        self.__name: str        = self.__data['name']
        self.__defname: str     = self.__data['defname']
        self.__description: str = self.__data['description']
        self.__code: list[list[str]] | str = self.__data['code']
    
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def defname(self):
        return self.__defname
    @property
    def description(self):
        return self.__description
    @property
    def code(self):
        return self.__code
    
    
    def get_code(self) -> str:
        try:
            if not isinstance(self.code, list):
                raise TypeError

            code = "\n".join(" ".join(i) for i in self.code)
            code = code.replace('M', Artifact.MATTER).replace('D', Artifact.DESIGN).replace('B', Artifact.BLOOD).replace('S', Artifact.SOUL)
            return code
        
        except TypeError:
            return str(self.code)
    
    #TODO
    # def unlock(self, unlocked: bool = True) -> None:
    #     if self.save_path is None:
    #         raise ValueError("No save path provided.")
        
    #     json_data = json.load(open(self.save_path))
    #     json_data["artifacts_unlocked"][self.id] = unlocked
    #     json.dump(json_data, open(self.save_path, 'w'))
    
    @property
    def unlocked(self) -> bool:
        if params["save_file_path"] is None:
            unlocked_artifacts: list[str] = []
        else:
            file = open(params["save_file_path"])
            unlocked_artifacts = regex.findall(r"<unlock>(Artifacts\.\w+)</unlock>", file.read())
        return self.defname in unlocked_artifacts

    @property
    def full_name(self) -> str:
        return f"Artifact of {self.name}"
    
    def __repr__(self) -> str:
        return f"Artifact(name='{self.name}', defname='{self.defname}', description='{self.description}')"
    
    def __hash__(self) -> int:
        return hash(self.id + self.name + self.defname + self.description + str(self.code))

LIST_OF_ARTIFACTS: dict[str, Artifact]
LIST_OF_ARTIFACTS = {name: Artifact(name) for name in json.load(open(os.path.join(os.path.dirname(__file__), 'artifacts.json')))}



class OpenArtifactCommand(Command):
    
    name = "open"
    description = "Open artifact details. Takes artifact name as argument."
    
    @property
    def arguments(self) -> Completion:
        return {i: None for i in LIST_OF_ARTIFACTS}
        
    
    def __call__(self, *args) -> None:
        
        if len(args) == 0 or args[0] not in LIST_OF_ARTIFACTS:
            raise ArgumentError("Please provide a valid artifact name as argument.")
        
        self.artifact = LIST_OF_ARTIFACTS[args[0]]
        
        print()
        print(("& " +self.artifact.full_name + " &").center(50, '='))
        print()
        print(*[i.center(50) for i in self.artifact.get_code().splitlines()], sep="\n")
        print()
        print(self.artifact.description.center(50))



class ListArtifactsCommand(Command):
    
    name = "list"
    description = "List all artifacts."
    
    def __call__(self, *args) -> None:
        print("Available Artifacts:")
        for artifact in LIST_OF_ARTIFACTS.values():
            status = "✓" if artifact.unlocked else "✗"
            print(f"- {artifact.full_name.ljust(30)} {status}")