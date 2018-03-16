import json

class SensorsData:
    def __init__(self, data):
        self.data = data

    def getData(self):
        data = self.data
        if isinstance(data, list):
            print("list")
        elif isinstance(data, str): 
            print("string")

        data2 = data[1:-1].split("}")
        print( " ... %d" % len(data2) )
        print("&&&1" + data2[0])
        print("&&&2" + data2[1])
        print("&&&" + data2[2])

        print( "wwww " + data[1:-1])
        d1 = json.loads(data2[0]+"}")
        ds = data2[1]
        d2 = json.loads(ds[1:]+"}")
        print("****", d1["type"])
        print("****", d2["value"])
        
        print(data)