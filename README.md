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

#### Custom attributes

All custom definition are in `custom.css` file.

## Input schema

Simple definition of a input file:

```python
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
```

