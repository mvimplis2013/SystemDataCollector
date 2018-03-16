import pycurl
from io import BytesIO
import json

import daiquiri
import logging

import re

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
    c.close()
    
    body = buffer.getvalue()
    plugins = body.decode('iso-8859-1')

    plugins = plugins[1: -1]
    plugins = plugins.replace('"', '')

    print( "..." , plugins )
    
    plugins_all = plugins.split(",")
    print( "--> ", plugins_all  )

    print( " 0 is ", len( plugins_all ) )
    print( plugins_all[9] )

    return plugins

