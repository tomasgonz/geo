import os
import importlib.resources

def get_groups():
    groups = []
    for i in importlib.resources.path(__package__, "groups").iterdir():
        groups.append(i.name.split(".")[0])
    return groups

def get_countries(group):
    countries = []
    path = group + ".json"
    file_path = importlib.resources.path(__package__, "countries.json")


        
    
    
    

