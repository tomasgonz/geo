import sys
from paises import Countries
from paises.groups import *

import importlib.resources

def test_countries():
    c = Countries()
    c.load_wb()
def test_groups():
    print(get_groups())