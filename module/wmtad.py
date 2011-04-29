import sys

class Parser:
    def __init__(self):
        pass
    def parse(self, message):
        results = {}
        for key, value in item_pattern.findall(line):
            match = item_pattern.match(value)
            if(match): #Case RN:ETC:20090324-15-01
                results[key] = u''
                results[match.group(1)] = match.group(2)
            else:
                results[key] = value
        sys.stderr.write("this is custom parser %s\n"%results)