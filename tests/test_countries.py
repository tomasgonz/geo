from paises import Countries
from paises import Groups

def test_countries():
    c = Countries()
    c.load_wb()

def test_groups():
    g = Groups()