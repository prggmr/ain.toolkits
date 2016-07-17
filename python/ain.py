# --encoding: utf-8 ---

# Python
import logging
import socket
import time
import json

log = logging.getLogger(__name__)

class Signal(object):
    """A signal within AIN.
    """
    def __init__(self, *args, **kwargs):
        self.__signal__ = self.__class__

class Connection(object):

    def __init__(self, host, port):
        log.info("Starting new AIN connection {0}:{1}".format(host, port))
        self.connection = socket.create_connection((host, port))
        self.connection.setblocking(0)
        
    def write(self, data):
        self.connection.send(data)

    def wait(self, timeout=1):
        time.sleep(timeout)

    def send_signal(self, signal):
        self.write(json.dumps([dict({
            "command": "dispatch_signal",
            "signal": str(signal)
        })]))

class HiSignal(Signal):
    pass

import time
import random
t = time.time()
i=1000
sleep_time=0
while(i>0):
    connection = Connection("0.0.0.0", 2444)
    connection.send_signal(HiSignal())
    while True:
        try:
            print connection.connection.recv(1024)
        except:
            pass
    connection.connection.close()
    i=i-1
    sleep=random.random()/1024
    sleep_time+=sleep
    time.sleep(sleep)
    # time.sleep(rand.random())
    
e = time.time()
print (e-t)-sleep_time
print sleep_time
print "Done"