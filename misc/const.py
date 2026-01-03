from typing import Literal
from rich.console import Console

COMMON_STYLE: dict[Literal['qmark', 'amark'], str]
COMMON_STYLE = {'qmark': '>', 'amark': '>'}

console = Console(highlight=False)