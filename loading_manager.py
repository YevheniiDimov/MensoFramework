from .input import Input
from .output import Output
from .module import Module
from .service import Service
import json
import os

class LoadingManager:
    """Load all modules from Modules folder"""
    def load_modules():
        modules = []
        for module in os.listdir('Modules'):
            if module.endswith('.json'):
                obj = json.load(open('Modules/' + module))
                modules.append(obj)
        return modules
    
    """Load all services from Services folder"""
    def load_services():
        services = []
        for service in os.listdir('Services'):
            if service.endswith('.json'):
                obj = json.load(open('Services/' + service))
                services.append(obj)
        return services
    
    """Load all inputs from Inputs folder"""
    def load_inputs():
        inputs = []
        for input in os.listdir('Inputs'):
            if input.endswith('.json'):
                obj = json.load(open('Inputs/' + input))
                inputs.append(obj)
        return inputs
    
    """Load all outputs from Outputs folder"""
    def load_outputs():
        outputs = []
        for output in os.listdir('Outputs'):
            if output.endswith('.json'):
                obj = json.load(open('Outputs/' + output))
                outputs.append(obj)
        return outputs