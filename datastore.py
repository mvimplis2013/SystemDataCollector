from sensorsdata import SensorsData

class SystemMetrics:
    def __init__(self):
        self.system_metrics = {
            "upTime": 0
        }

    def setUpTimeData(self, value):
        self.system_metrics["upTime"] = value

    def setSensorsData(self, value):
        sensorsData = SensorsData(value)
        self.system_metrics["sensors"] = sensorsData

    def getUpTimeData(self):
        return self.system_metrics["upTime"]

    def getSensorsData(self):
        return self.system_metrics["sensors"].getData()
