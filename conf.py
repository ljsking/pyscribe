import ConfigParser

def load_config(conf_file_path):
    config = ConfigParser.ConfigParser()
    config.read(conf_file_path)
    return config

def get_parsers(parsers):
    results = {}
    for parser in parsers:
        category = parser[0]
        class_full_name = parser[1]
        
        splited = class_full_name.split('.')
        module_name = '.'.join(splited[:-1])
        class_name = splited[-1]
        
        module = __import__(module_name)
        results[parser[0]] = getattr(module, class_name)()
    return results