import json

class Service:
    """Create service class with name, model, dependencies (another services) and hash"""
    def __init__(self, name, model, dependencies):
        self.name = name
        self.model = model
        self.dependencies = dependencies
        self.hash = hash(self)
        
    """Make a prediction from model using dependencies predictions"""
    def predict(self):
        results = []
        for dependency in self.dependencies:
            results.append(dependency.predict())
            
        return self.model.predict(results)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)