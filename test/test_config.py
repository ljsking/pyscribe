import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(os.path.join(os.path.dirname(__file__),'..','module'))

from conf import load_config, get_parsers
import unittest

class TestConfig(unittest.TestCase):

    def setUp(self):
        test_dir=os.path.dirname(__file__)
        self.conf_file = os.path.join(test_dir,"..","conf","pyscribe.conf")

    def test_load(self):
        config = load_config(self.conf_file)
        self.assertEquals(9999, config.getint('common', 'port'))
        self.assertEquals([('ncs_index_err','ncs_index_err.Parser')], config.items('parsers'))
        
    def test_get_parsers(self):
        config = load_config(self.conf_file)
        parsers = get_parsers(config.items('parsers'))
        self.assertEquals(1, len(parsers))
        self.assertEquals("ncs_index_err", parsers['ncs_index_err'].__class__.__module__)
        self.assertEquals("Parser", parsers['ncs_index_err'].__class__.__name__)
        
if __name__ == '__main__':
    unittest.main()