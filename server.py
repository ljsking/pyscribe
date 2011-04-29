#!/usr/bin/env python

import sys
sys.path.append('./gen-py')
sys.path.append('./module')

from scribe import *
from scribe.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import handler
import conf
import logging

users = []

#set logging
logging.basicConfig(level=logging.INFO)

#read configure file
config = conf.load_config('conf/pyscribe.conf')

handler = handler.LogHandler()
#set parsers
handler.parsers = conf.get_parsers(config.items('parsers'))

processor = scribe.Processor(handler)
transport = TSocket.TServerSocket(config.getint('common', 'port'))
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'