from typing import Literal

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

COMMON_STYLE: dict[Literal['qmark', 'amark'], str]
COMMON_STYLE = {'qmark': '>', 'amark': '>'}

class Highlighter(RegexHighlighter):
    base_style = "highlight."
    highlights = [
        r"(?P<quote>')",
        r"(?P<content>(?<=')[^']*(?='))",
        r"(?P<err>(ERROR))",
        r"(?P<err>(PLACEHOLDER))"
    ]

theme = Theme({
    "highlight.quote": "green",
    "highlight.content": "yellow",
    
    "highlight.err": "red bold"
})

console = Console(theme=theme, highlighter=Highlighter())