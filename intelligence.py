from .input import Input
from .output import Output
from .module import Module
from .service import Service

class Intelligence:
    """Create a class of intelligence which contains inputs, outputs, modules and services"""
    def __init__(self, inputs, outputs, modules, services):
        self.inputs = inputs
        self.outputs = outputs
        self.modules = modules
        self.services = services
        
    """Get all data from inputs"""
    def get_input_data(self):
        data = {}
        for input in self.inputs:
            data[input.name] = input.get_data()
        return data
    
    """Activate regulator service in services with input data"""
    def activate_regulator(self):
        self.services['Regulator'].activate(self.get_input_data())
    