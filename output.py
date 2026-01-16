from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

from misc.enums import Rarity

def _make_regex():
    for i in Rarity:
        yield rf"(?P<R{i.name}>{i.value})"

class _Highlighter(RegexHighlighter):
    base_style = "highlight."
    highlights = [
        r"(?P<quote_content>'[^']*')",
        r"(?P<quote>')",
        r"(?P<err>(ERROR))",
        r"(?P<err>(PLACEHOLDER))",
    ] + list(_make_regex())

_theme = Theme({
    "highlight.quote_content": "yellow",
    "highlight.quote": "green",
    
    "highlight.err": "red bold",
    
    "highlight.RCommon": "white",
    "highlight.RUncommon": "green",
    "highlight.RLegendary": "red",
    "highlight.RBoss": "yellow",
    "highlight.RPlanet": "yellow",
    "highlight.RLunar": "blue",
    "highlight.RVoid": "magenta",
    "highlight.RMeal": "#FF5C00",
    "highlight.REquipment": "#FFA500",
    "highlight.RElite": "#FF5C00",
    "highlight.RUsed": "dim #808080",
})

console = Console(theme=_theme, highlighter=_Highlighter())