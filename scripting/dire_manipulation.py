#!/usr/bin/env python
# import requirements
import os

for file in os.listdir():
    if file.endswith(".py"):
        os.system(f"cat {file}")


