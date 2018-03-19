import json

import logging
import daiquiri

daiquiri.setup( level=logging.DEBUG )
logger = daiquiri.getLogger()

class CommonData(object):
    def __init__(self, data=""):
        self.total_metrics = []

        # Input data is ... String
        # Decode JSON into a list ... Key/ Values
        self.json_data = json.loads( data )
        
    def populate(self, section, total_keys, preferred_keys):
        self.total_metrics.append(section);
        print( "&&& " + str( self.total_metrics ) )

        # For every key-metric 
        for tk in total_keys:
            # Read the measured value
            tk_val = self.json_data[tk]

            self.total_metrics[section]



            
        return
        
    def getAllJSONData(self):
        return self.json_data
