import os
from pathlib import Path
from pprint import pprint

path = Path('.')

funcs = [fun for fun in dir(path) if not fun.startswith('_')]

pprint(funcs)
