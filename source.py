import requests

class Source:
    """Create source class which contains url and data format"""
    def __init__(self, url, data_format):
        self.url = url
        self.data_format = data_format
        
    """Fetch data from url in specified format"""
    def fetch_data(self):
        if self.data_format == 'json':
            return requests.get(self.url).json()
        elif self.data_format == 'xml':
            return requests.get(self.url).text
        else:
            return None
    
    """Post data to url in specified format"""
    def post_data(self, data):
        if self.data_format == 'json':
            return requests.post(self.url, json=data)
        elif self.data_format == 'xml':
            return requests.post(self.url, data=data)
        else:
            return None