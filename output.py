from .source import Source
import json 

class Output:
    """Create an output class which contains a source and a name"""
    def __init__(self, source, name):
        self.source = source
        self.name = name
        
    """Post data to source"""
    def post_data(self, data):
        return self.source.post_data(data)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)