import pycurl
from io import BytesIO
import json

import daiquiri
import logging

from pluginslist import get_pluginslist 

# Time-Now and Sleep-Msecs
import time
from datetime import datetime 

# Easy Logging Mechanim with Colors
daiquiri.setup( level = logging.DEBUG )
logger = daiquiri.getLogger()

""" System Data Collection Mechanism is Responsible for Sets:
1) System information (Ubuntu 16.04 64bit / Linux 4.4.0-57-generic)
2) IP addresses
2) Docker Containers
3) File System Used/ Total
4) Disk I/O
.... ALERT logs
""" 
def collect_system_data():
    now = datetime.now().time();
    logger.info( "Ready to Collect Current System Data ..." );

    plugins = get_pluginslist()
    logger.debug(plugins)

    buffer = BytesIO()

    c = pycurl.Curl()
    c.setopt(c.URL, 'http://localhost:61208/api/2/mem')
    c.setopt(c.WRITEDATA, buffer)

    c.perform()
    c.close()

    body = buffer.getvalue()
    logger.debug(body.decode('iso-8859-1'))

    try:
        json_object = json.loads(body.decode('iso-8859-1'))
    except ValueError as e:
        logger.error("REST API Response JSON Load Failure: ", e)

    mem = {}
    mem["total"] = json_object["total"]
    mem["cached"] = json_object["cached"]
    mem["active"] = json_object["active"]
    logger.debug(mem)

if __name__ == '__main__':
    collect_system_data() 