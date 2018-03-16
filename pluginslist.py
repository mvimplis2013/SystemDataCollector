import pycurl
from io import BytesIO
import json

import daiquiri
import logging

# the module with all system-metrics handlers
import allgetters

# Global variables to share data across modules
import globalvars

loglevel = globalvars.loglevel;
pluginslist_uri = globalvars.pluginslist_uri
# EndOfGlobals

""" DAIQUIRI is a tiny library: Configure the Python 
logging subsystem. Use colors if logging to a terminal. 
"""
daiquiri.setup( loglevel )
logger = daiquiri.getLogger()

def get_pluginslist():
    buffer = BytesIO()

    c = pycurl.Curl()
    c.setopt( c.URL, pluginslist_uri )
    c.setopt( c.WRITEDATA, buffer )
    
    c.perform()
    #c.close()
    
    body = buffer.getvalue()
    plugins = body.decode('iso-8859-1')

    # remove first and last character ... {}
    # remove double-quotes ... From "item" To item 
    plugins = plugins[1: -1]
    plugins = plugins.replace('"', '')

    # make the [plugins]
    plugins_all = plugins.split(",")    
    print( "Plugins Found --> ", len( plugins_all ) )
    
    # for each : plugin
    for p in plugins_all:
        rest_api = globalvars.glance_rest_json_api
        pclean = p.strip()
        api = rest_api + pclean
        
        # clear buffer ... avoid concatenation
        buffer.truncate(0)
        buffer.seek(0)

        # curl http://localhost:16208/api/2/<plugin>
        c.setopt( c.URL, api )
        c.perform()

        # get specific system-metric ... "mem", "cpu" 
        body = buffer.getvalue()
        response = body.decode('iso-8859-1')

        # for every system-metric .. an appropriate response Hander
        function_a = getattr(allgetters, "get_" + pclean) 
        function_a( response )
        
    return plugins

