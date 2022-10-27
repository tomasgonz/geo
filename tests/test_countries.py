from paises import Countries
from paises.groups import *

def test_countries():
    c = Countries()
    c.load_wb()

def test_groups():
    print(load_groups())