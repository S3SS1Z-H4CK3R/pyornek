#!/usr/bin/python

import sys,time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

slowprint("\x1b[03;36mThis tool was created by S3SS!Z H4CK3R")
