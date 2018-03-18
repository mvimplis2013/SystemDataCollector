from sensorsdata import SensorsData
from memorydata import MemoryData
from cpudata import CpuData

class SystemMetrics:
    def __init__(self):
        self.system_metrics = {}

    def setUpTimeData(self, value):
        self.system_metrics["upTime"] = value

    def setSensorsData(self, value):
        sensorsData = SensorsData(value)
        self.system_metrics["sensors"] = sensorsData

    def setMemoryData(self, value):
        self.system_metrics["memory"] = MemoryData(value)

    def setCpuData(self, value):
        self.system_metrics["cpu"] = CpuData(value)
        
    def getUpTimeData(self):
        return self.system_metrics["upTime"]

    def getSensorsData(self):
        return self.system_metrics["sensors"].getData()

    def getMemoryData(self):
        return self.system_metrics["memory"].getData()

    def getCpuData(self):
        self.system_metrics['cpu'].populate()
        
        return self.system_metrics["cpu"].getOneKey()