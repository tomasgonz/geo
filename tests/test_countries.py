from paises import Countries
from paises import Groups
from paises.alias import get_alias

def test_countries():
    c = Countries()
    c.load_wb()

def test_groups():
    g = Groups()

def test_alias():
    print(get_alias(['Bangladesh', 'Congo', 'Uganda']))
