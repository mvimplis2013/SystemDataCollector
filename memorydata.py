import json

class MemoryData:
    def __init__(self, data):
        print("..." + data)
        self.data = json.loads(data)

    def getData(self):
        print(self.data["total"])


        
    
    