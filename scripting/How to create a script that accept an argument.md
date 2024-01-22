# How to create a script that accept an argument

## Script 

```
import base64
import os
import json
import argparse
from collections import OrderedDict
import hashlib
from zipfile import ZipFile

FILE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "../files/"
))

def open_file(file_name):
    file = os.path.normpath(os.path.join(FILE_DIR, file_name))
    with open(file) as fp:
        return json.load(fp, object_pairs_hook=OrderedDict)

def process(file_name):
    file = open_file(file_name)
    print(json.dumps(file, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help = "Automation file Name", nargs="*",
                        default = None)
    args = parser.parse_args()
    process(args.file_name[0])
```

## Command 
```
script.py --file $(FILE_NAME) > ./Output/$(FILE_NAME)
```

