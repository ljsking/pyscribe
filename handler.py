from scribe.ttypes import ResultCode

class LogHandler:
	def __init__(self):
		self.parsers = {}

	def Log(self, entries):
	    for entry in entries:
	        if entry.category in self.parsers:
	            parser = self.parsers[entry.category]
	            parser.parse(entry.message)
		return ResultCode.OK