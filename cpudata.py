from __future__ import absolute_import, unicode_literals

from basedata import CommonData
from config import Config

class CpuData(CommonData):
    def __init__(self, data):
        CommonData.__init__(self, data)
        self.config = Config()
        
        # Let the user select the list of interesting cpu-activity metrics
        self.cpu_user_preferences = self.config.parser.get(
            "cpu", "user_preferences")

        # the whole set of cpu-data that linux is providing 
        self.all_keys = {
            'cpucore',
            'ctx_switches',
            'irq',
            'syscalls',
            'steal',
            'guest',
            'system',
            'idle',
            'interrupts',
            'softirq',
            'time_since_update',
            'guest_nice',
            'soft_interrupts',
            'user',
            'total',
            'nice',
            'iowait',
        }

        self.cpu_metrics = {}
        self.populate()

        # EndOf __init__
        return
    
    """ Parse JSON data and save key/Value pairs for 
    important cpu-metrics """
    def populate(self):
        # For every key-metric 
        for tk in self.all_keys:
            # Read the measured value
            tk_val = self.json_data[tk]

            # Append Key/ Value pair to total-metrics dictionary 
            self.cpu_metrics[tk] = tk_val
        
        # Finished JSON data parsing ... 
        # from lengthy string to Key/ Values
        
        return

    """ Start GETting specific measurements
    Call the appropriate get_interesting() """
    def get_cpucore(self):
        return self.cpu_metrics["cpucore"]

    def get_ctxswitches(self):
        return self.cpu_metrics["ctx_switches"]

    def get_irq(self):
        return self.cpu_metrics["irq"]

    def get_syscalls(self):
        return self.cpu_metrics["syscalls"]
         
    def get_steal(self):
        return self.cpu_metrics["steal"]

    def get_guest(self):
        return self.cpu_metrics["guest"]

    def get_system(self):
        return self.cpu_metrics["system"]
    
    def get_idle(self):
        return self.cpu_metrics["idle"]
    
    def get_interrupts(self):
        return self.cpu_metrics["interrupts"]
    
    def get_softirq(self):
        return self.cpu_metrics["softirq"]

    def get_timesinceupdate(self):
        return self.cpu_metrics["time_since_update"]

    def get_guestnice(self):
        return self.cpu_metrics["guest_nice"]  

    def get_softinterrupts(self):
        return self.cpu_metrics["soft_interrupts"]

    def get_user(self):
        return self.cpu_metrics["user"]

    def get_total(self):
        return self.cpu_metrics["total"]

    def get_nice(self):
        return self.cpu_metrics["nice"]

    def get_iowait(self):
        return self.cpu_metrics["iowait"]
        
    def getAllData(self):
        print("Kopanos")
        return self.getAllJSONData()