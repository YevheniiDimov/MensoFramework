from .source import Source

class Output:
    """Create an output class which contains a source and a name"""
    def __init__(self, source, name):
        self.source = source
        self.name = name
        
    """Fetch data from source and return it"""
    def fetch_data(self):
        return self.source.fetch_data()