"""
# Config file
USER=admin
PORT=8080
ENABLE_LOGS=true
# This is a comment
TIMEOUT=30

{
  "USER": "admin",
  "PORT": 8080,
  "ENABLE_LOGS": True,
  "TIMEOUT": 30
}

"""
# import str # type: ignore
import os 
from pathlib import Path
import pathlib

class ConfigParser():
    def __init__(self, file):
        self.file = file
        self.op = {}

    def ReadFile(self):
        with open(self.file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    yield line

    def ProcessLines(self, line):
        key, value = map(str.strip, line.split("="))
        if value == 'true':
            value = True
        elif value == 'false':
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    value = value
        self.op[key] = value
    
    def parse(self):
        for line in self.ReadFile():
            self.ProcessLines(line)
        return self.op

if __name__ == '__main__':
    from pathlib import Path
    processor = ConfigParser("./data/config.cfg")
    d = processor.parse()
    print(d)


