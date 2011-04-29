from scribe.ttypes import ResultCode
import logging

logger = logging.getLogger("Loghandler")

class LogHandler:
    def __init__(self):
        self.parsers = {}

    def Log(self, entries):
        for entry in entries:
            if entry.category in self.parsers:
                parser = self.parsers[entry.category]
                logger.debug("%s:%s", entry.category, entry.message)
                parser.parse(entry.message)
            else:
                logger.debug("no category %s:%s", entry.category, entry.message)
        return ResultCode.OK