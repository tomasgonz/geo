import sys
from paises import *

def test_countries():
    c = Countries()
    c.load_wb()
    print ("test for countries passes")

if __name__ == "__main__":
    test_countries()