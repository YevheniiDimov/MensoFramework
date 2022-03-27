import json

class Module:
    """Create module class with name, model, dependencies (another modules) and hash"""
    def __init__(self, name, model, dependencies, hash):
        self.name = name
        self.model = model
        self.dependencies = dependencies
        self.hash = hash
        
    """Make a prediction from model using dependencies predictions"""
    def predict(self):
        """Get all predictions from predict method of dependencies"""
        results = []
        for dependency in self.dependencies:
            results.append(dependency.predict())
            
        return self.model.predict(results)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)