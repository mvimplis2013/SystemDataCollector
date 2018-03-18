from __future__ import absolute_import, unicode_literals

from basedata import CommonData

class CpuData(CommonData):
    def __init__(self, data):
        CommonData.__init__(self, data)

        self.cpu = {
            'key',
            'cpu_number',
            'user',
            'system',
            'idle',
        }

    def populate(self):
        CommonData.populate( self.cpu )
        
    def getOneKey(self):
        return 'a'#self.cpu['key']

    def getAllData(self):
        print("Kopanos")
        return self.getAllJSONData()