#!/usr/bin/env python

import sys

if 'fail' in sys.argv:
    print 'Test failed.'
    sys.exit(1)
print 'Test succeeded.'
sys.exit(0)
