from dataclasses import dataclass, field
from typing import List, Literal

Color = Literal['Primary', 'Secondary',
                'Success', 'Danger',
                'Warning', 'Info',
                'Light', 'Dark']


@dataclass
class Link:
    """
    Single link, shown as a button.

    Args:
        name: Text inside button.
        url: Any address (supported by web-browser).
        notes: Additional information in tooltip.
            Default: None.
        color: Color of a button.
            Default: Secondary.
    """
    name: str
    url: str
    notes: str = None
    color: Color = 'secondary'


@dataclass
class Section:
    """
    Box (Bootstrap's Card) with Button links.

    Args:
        name: Title of a Card.
        notes: Additional information in tooltip.
            Default: None
        color: Color of a Card's header/title.
            Default: Primary.
        links: List of `Link`s to put inside.
    """
    name: str
    notes: str = None
    color: Color = 'primary'
    links: List[Link] = field(default_factory=list)


@dataclass
class Board:
    """Represent the Dashboard.

    Attrs:
        name: Name of the page. Also placed in navbar and in page title.
            Default: Dashboard
        navbar: List of `Link`s to put in navbar section.
            Default: []
        sections: List of `Section`s.
            Default: []
    """
    name: str = field(default="Dashboard")
    navbar: List[Link] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
