#!/usr/bin/env python
# Parallel change B.
import sys

if 'fail' in sys.argv:
    print 'Test failed.'
    sys.exit(1)
print 'Test succeeded.'
sys.exit(0)
#topic b
# change to master
#test br1
#test br1 2
#test merge
#merge
