import json
import importlib.resources

class groups(list):
	
	def __init__(self):
		if len(self) == 0:
			pass

	def load_groups(self):
		for i in importlib.resources.path(__package__, "groups").iterdir():
			print("Loading " + i.name)
			self.append(json.load(i.open(encoding='utf-8')))

		return groups
	
	def get_countries(self, group):
		countries = []
		path = group + ".json"
		file_path = importlib.resources.path(__package__, "countries.json")