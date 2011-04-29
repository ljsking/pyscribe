import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','gen-py'))

from handler import LogHandler

from scribe.ttypes import *
import unittest

class TestParser(object):
    def __init__(self):
        self.logger = []
    def parse(self, message):
        self.logger.append(message)

class TestLogHandler(unittest.TestCase):

    def setUp(self):
        pass

    def test_load(self):
        handler = LogHandler()
        test_parser = TestParser()
        handler.parsers = {'test':test_parser}
        entry = LogEntry(category='test', message='test')
        handler.Log([entry])
        self.assertEquals(['test'], test_parser.logger)
        
if __name__ == '__main__':
    unittest.main()