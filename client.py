#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from scribe import *
from scribe.ttypes import *

from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol

category = 'ncs_index_err'
message = 'test_message'

host = 'localhost'
port = 9999

log_entry = LogEntry(category=category, message=message)

socket = TSocket.TSocket(host=host, port=port)
transport = TTransport.TFramedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(trans=transport, strictRead=False, strictWrite=False)
client = scribe.Client(iprot=protocol, oprot=protocol)

transport.open()
result = client.Log(messages=[log_entry])
transport.close()