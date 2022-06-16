import logging
import os
from pathlib import Path
from typing import List, TypedDict, Union

import yaml
from jinja2 import FileSystemLoader, Template, Environment

logger = logging.getLogger(__name__)


class Link(TypedDict,
           total=False):
    name: str
    notes: str
    url: str


class Section(TypedDict,
              total=False):
    name: str
    notes: str
    links: List[Link]


class Board(TypedDict,
            total=False):
    nav: List[Link]
    sections: List[Section]


SPath = Union[str, Path]


class BoardRenderer:

    def __init__(self,
                 data: SPath,
                 template: SPath = "./template/base.html",
                 output: SPath = "./dashboard"
                 ):
        self.data = data
        self.template = template
        self.output = output

        self.template_dir = os.path.dirname(self.template)
        self.template_file = os.path.basename(self.template)

    def render(self,
               path=None
               ):
        if path is None:
            path = self.output
        try:
            data = self._load_data()
            template = self._load_template()
            render = template.render(data)
        except Exception as ex:
            raise ValueError("Render error.") from ex

        self._save_output(render, path)
        return path

    def _load_data(self) -> Board:
        logger.debug(
            f"Loading data file from [{self.data}]")

        with open(self.data, mode="r") as f:
            yaml_data = yaml.safe_load(f)
            logger.debug(
                f"Data from [{self.data}] loaded.")
        return Board(**yaml_data)

    def _load_template(self) -> Template:
        template_dir = os.path.dirname(self.template)
        logger.debug(
            f"Setting up Environment in path [{self.template}]")
        env = Environment(
            loader=FileSystemLoader(self.template_dir))
        return env.get_template(self.template_file)

    def _save_output(self,
                     data: str,
                     path: str
                     ) -> str:
        logger.debug(
            f"Saving data [ID:{id(data)}] to path [{path}]")
        with open(path, mode="w+") as f:
            f.writelines(data)
        logger.debug(f"Data [ID:{id(data)}] saved.")

        return path
