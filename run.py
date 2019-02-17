#!/usr/bin/env python

import sys, os
import hashlib
from avatar import create_avatar

if len(sys.argv) != 2:
  print 'Usage: run.py your.email@server.com'
  sys.exit()

email = sys.argv[1] # account email address is the basis for the hash
size = 512          # [size] x [size] pixels
output = "unicorn.bmp"

hash = hashlib.md5(email).hexdigest()

# Creates a BMP file of 256x256 pixels (see docstring of create_avatar)
f = open(output, "wb")
f.write(create_avatar(size, int(hash, 16)))
f.close()
