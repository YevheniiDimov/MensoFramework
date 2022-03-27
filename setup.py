from intelligence import Intelligence
from loading_manager import LoadingManager
from keras.models import Sequential
from keras.layers import Dense
from module import Module
from service import Service
from input import Input
from output import Output
from source import Source
from url import Url
import colorama

"""Create an intelligence instance and load all components"""
def load():
    print(colorama.Fore.CYAN + 'Loading Intelligence:' + colorama.Fore.RESET)
    
    print(colorama.Fore.BLUE + '\tLoading Inputs...' + colorama.Fore.RESET)
    inputs = LoadingManager.load_inputs()
    print(colorama.Fore.BLUE + '\tLoading Outputs...' + colorama.Fore.RESET)
    outputs = LoadingManager.load_outputs()
    print(colorama.Fore.BLUE + '\tLoading Modules...' + colorama.Fore.RESET)
    modules = LoadingManager.load_modules()
    print(colorama.Fore.BLUE + '\tLoading Services...' + colorama.Fore.RESET)
    services = LoadingManager.load_services()
    
    print(colorama.Fore.GREEN + '\nAll components are loaded.' + colorama.Fore.RESET)
    
    intelligence = Intelligence(inputs, outputs, modules, services)
    
    print(colorama.Fore.GREEN + 'Intelligence is ready.' + colorama.Fore.RESET)
    
    return intelligence

"""Creates intelligence, console input, console output, perceptron module and regulator service and adds them to intelligence"""
def create_intelligence():
    model = Sequential()
    model.add(Dense(1, input_dim=1, activation='sigmoid'))
    
    print(colorama.Fore.CYAN + 'Creating Intelligence:' + colorama.Fore.RESET)
    
    print(colorama.Fore.BLUE + '\tCreating Inputs...' + colorama.Fore.RESET)
    inputs = [Input(Source(Url('Console', 'console'), 'json'), 'ConsoleInput')]
    print(colorama.Fore.BLUE + '\tCreating Outputs...' + colorama.Fore.RESET)
    outputs = [Output(Source(Url('Console', 'console'), 'json'), 'ConsoleOutput')]
    print(colorama.Fore.BLUE + '\tCreating Modules...' + colorama.Fore.RESET)
    modules = [Module('Perceptron', model, [])]
    print(colorama.Fore.BLUE + '\tCreating Services...' + colorama.Fore.RESET)
    services = [Service('Regulator', model, [])]
    
    print(colorama.Fore.GREEN + '\nAll components are created.' + colorama.Fore.RESET)
    
    intelligence = Intelligence(inputs, outputs, modules, services)
    
    print(colorama.Fore.GREEN + 'Intelligence is ready.' + colorama.Fore.RESET)
    
    return intelligence