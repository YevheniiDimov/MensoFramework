from source import Source
import json

class Input:
    """Create an input class which contains a source and a name"""
    def __init__(self, source, name):
        self.source = source
        self.name = name
        
    """Fetch data from source and return it"""
    def fetch_data(self):
        return self.source.fetch_data()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)