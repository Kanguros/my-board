import logging

import logging
import os
from pathlib import Path
from typing import List, TypedDict, Union, Literal

import yaml
from jinja2 import FileSystemLoader, Template, Environment

logger = logging.getLogger(__name__)

Color = Literal['Primary', 'Secondary',
                'Success', 'Danger',
                'Warning', 'Info',
                'Light', 'Dark']


class Link(TypedDict,
           total=False):
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
    notes: str
    color: Color


class Section(TypedDict,
              total=False):
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
    notes: str
    color: Color
    links: List[Link]


class Board(TypedDict,
            total=False):
    """Represent the Dashboard.

    Attrs:
        name: Name of the page. Also placed in navbar and in page title.
            Default: Dashboard
        navbar: List of `Link`s to put in navbar section.
            Default: []
        sections: List of `Section`s.
            Default: []
    """
    name: str
    navbar: List[Link]
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

    def render(self,
               path=None
               ):
        if path is None:
            path = self.output

        try:
            logger.info(f"Loading input data...")
            data = self._load_data()
            logger.info(f"Loading template...")
            folder = os.path.dirname(self.template)
            main_file = os.path.basename(self.template)

            template = self._load_template(folder, main_file)
            logger.info(f"Rendering a page...")

            render = template.render(data)
        except Exception as ex:
            logger.error(f"Re")
            raise ValueError("Render error.") from ex

        logger.info(f"Page rendered. Saving output in {path}")
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

    def _load_template(self, folder, main_file) -> Template:
        logger.debug(
            f"Setting up Environment in path [{folder}]")
        env = Environment(
            loader=FileSystemLoader(folder))

        logger.debug(
            f"Setting Template as [{main_file}]")
        return env.get_template(main_file)

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
