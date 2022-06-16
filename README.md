# Links Dashboard

Single HTML local page with sections, links and other utilities, generated based on input from YAML file. 

----



`links.yaml`

```yaml
sections:
  - name: Search Engines
    notes: "Short Section description"
    links:
      - name: Google
        notes: "Short note which appear as a tooltip."
        url: https://google.com
      - name: DuckDuck
        notes: "Short note which appear as a tooltip."
        url: https://google.com
  - name: Usefull
    notes: "Short Section description"
    links:
      - name: GitHub
        notes: "Short note which appear as a tooltip."
        url: https://github.com
      - name: Wykop
        notes: "Short note which appear as a tooltip."
        url: https://wykop.pl
```



<img src="C:\Users\Kadu\AppData\Roaming\Typora\typora-user-images\image-20220616073331038.png" alt="image-20220616073331038" style="zoom:80%;" />



## How to use

1.   Install requirements 

     -   `pyproject.toml` -> `poetry install` 
     -   `requirements.txt` -> `pip install requirements.txt`

2.   Fill `links.yaml` with data

3.   Run `python .\script.py` from inside 

     

     

## Template

Page is generated using `jinja` templating engine. It consist of files:

-   `base.html` - Main file, include the rest ones.
-   `cards.html `- Whole content is here. Display cards with links inside.
-   `footer.html` - Bottom *navbar*.
-   `nav.html` - File for navbar.

## Theme

Bootstrap theme is used called **Now-UI Kit**

-   https://github.com/creativetimofficial/now-ui-kit

-   https://demos.creative-tim.com/now-ui-kit/docs/1.0/getting-started/introduction.html?ref=adnp-readme

#### Custom CSS

All custom definition are in `.\dashboard\assets\css\custom.css` file.

## Data schema

Definition of an input data file structure.


```python
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
```

#### Colors

Default BS's *colors* are used: `Primary, Secondary, Success, Danger, Warning, Info, Light, Dark`



_Usually, such definitions helps me not to remember the data's structure names I'm working with. 
The IDE hints take care of that. I did not foresee one thing. 
Referencing a variable in Jinja template is a, lets say, context less. No hints popup...
Nevertheless, it is a good reference point how the data in YAML should look like._

