import json

class CommonData(object):
    def __init__(self, data={}):
        self.json_data = data
        self.validate_json()
        
    def validate_json(self):
        try:
            json.loads( self.json_data )
        except Exception as ex:
            print("Disaster ..." + str(ex))
        
    def populate(keys_list):
        print(keys_list)
        
    def getAllJSONData(self):
        return self.json_data
