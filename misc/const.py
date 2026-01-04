from typing import Literal

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

COMMON_STYLE: dict[Literal['qmark', 'amark'], str]
COMMON_STYLE = {'qmark': '>', 'amark': '>'}

class QuoteHighlighter(RegexHighlighter):
    base_style = "quote."
    highlights = [
        r"(?P<quote>')",
        r"(?P<content>(?<=')[^']*(?='))",
    ]

theme = Theme({
    "quote.quote": "green",
    "quote.content": "yellow",
})

console = Console(theme=theme, highlighter=QuoteHighlighter())