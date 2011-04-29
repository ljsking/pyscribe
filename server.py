#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from scribe import *
from scribe.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

users = []

class LogHandler:
	def __init__(self):
		pass
		#self.log = {}

	def Log(self, entries):
	    for entry in entries:
	        print '%s:%s'%(entry.category, entry.message)
		return ResultCode.OK



handler = LogHandler()
processor = scribe.Processor(handler)
transport = TSocket.TServerSocket(9999)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'