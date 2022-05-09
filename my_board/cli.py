from dataclasses import field, dataclass, asdict
from pathlib import Path
from typing import List

import yaml
from jinja2 import FileSystemLoader, Template


@dataclass
class Link:
    name: str
    notes: str = ""
    link: str = ""


@dataclass
class Section:
    name: str
    notes: str = ""
    links: List[Link] = field(default_factory=list)


@dataclass
class BoardSchema:
    sections: List[Section] = field(default_factory=list)


class Board:

    def __init__(self,
                 data: Path,
                 template: Path = "./template"
                 ):
        self.data = data
        self.template = template

    def _load_data(self) -> BoardSchema:
        with open(self.data, mode="r") as f:
            return yaml.safe_load(f)

    def _load_template(self) -> Template:
        with open(self.template, mode="r") as f:
            return Template(f.read())

    def _save_output(self, data: str, path: str) -> str:
        with open(path, mode="w+") as f:
            f.writelines(data)
        return path

    def render(self, path):
        try:
            data = self._load_data()
            template = self._load_template()
            render = template.render(asdict(data))
        except Exception as ex:
            print(f"{ex}")
        else:
            return self._save_output(render, path)


