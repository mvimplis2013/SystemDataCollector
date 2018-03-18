import json

class SensorsData:
    def __init__(self, data):
        self.data = data

    def getData(self):
        data = self.data
        
        data2 = data[1:-1].split("}")
        
        d1 = json.loads( data2[0]+"}" )
        
        ds = data2[1]
        d2 = json.loads( ds[1:]+"}" )
        
        return [d1, d2]