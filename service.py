class Service:
    """Create service class with name, model, dependencies (another services) and hash"""
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
    
    