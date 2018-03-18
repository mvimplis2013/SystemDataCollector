from datastore import SystemMetrics 
from colorama import Fore, Back, Style 

import json

systemMetrics = SystemMetrics()

def get_sensors(response):
    print('Inside Handler "Sensors" ...')
    systemMetrics.setSensorsData(response);
    sensors = systemMetrics.getSensorsData()
    for s in sensors:
        print( "Sensor i --> " + json.dumps(s) )
        print('-------------------------------------------')

    return 

def get_network(response):
    #print("Inside Handler ... " + response)
    return

def get_percpu(response):
    #print("Inside Handler ... " + response)
    return

def get_load(response):
    #print("Inside Handler ... " + response)
    return

def get_uptime(response):
    print('Inside Handler "UpTime" ...')
    systemMetrics.setUpTimeData(response)
    print(systemMetrics.getUpTimeData())

    return

def get_processcount(response):
    #print("Inside Handler ... " + response)
    return

def get_quicklook(response):
    #print("Inside Handler ... " + response)
    return

def get_amps(response):
    #print("Inside Handler ... " + response)
    return

def get_folders(response):
    #print("Inside Handler ... " + response)
    return

def get_diskio(response):
    #print("Inside Handler ... " + response)
    return

def get_processlist(response):
    #print("Inside Handler ... " + response)
    return

def get_ports(response):
    #print("Inside Handler ... " + response)
    return

def get_raid(response):
    #print("Inside Handler ... " + response)
    return

def get_batpercent(response):
    #print("Inside Handler ... " + response)
    return

def get_gpu(response):
    #print("Inside Handler ... " + response)
    return

def get_memswap(response):
    #print("Inside Handler ... " + response)
    return

def get_ip(response):
    #print("Inside Handler ... " + response)
    return

def get_cpu(response):
    print( Back.YELLOW + 'Inside Handler "CPU"... ' + response )
    print( Style.RESET_ALL )

    systemMetrics.setCpuData( response )
    print( systemMetrics.getCpuData() )

    return

def get_fs(response):
    #print("Inside Handler ... " + response)
    return

def get_irq(response):
    #print("Inside Handler ... " + response)
    return

def get_help(response):
    #print("Inside Handler ... " + response)
    return

def get_core(response):
    #print("Inside Handler ... " + response)
    return

def get_mem(response):
    print('Inside Handler "Memory" ... ' + response)
    systemMetrics.setMemoryData(response)
    print(systemMetrics.getMemoryData())
    return

def get_docker(response):
    #print("Inside Handler ... " + response)
    return

def get_now(response):
    #print("Inside Handler ... " + response)
    return

def get_system(response):
    #print("Inside Handler ... " + response)
    return

def get_wifi(response):
    #print("Inside Handler ... " + response)
    return
    
def get_psutilversion(response):
    #print("Inside Handler ... " + response)
    return

def get_cloud(response):
    #print("Inside Handler ... " + response)
    return

def get_alert(response):
    #print("Inside Handler ... " + response)
    return