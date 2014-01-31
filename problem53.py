"""
What I did was stopped calculating when i first encountered > 1Million, and calculated manually from that point.
The different formula for even and odd "n", i found by observing nCr results from 23,24,25,26,27.
Using GMPY library with Python made this extremely fast. < 1ms
"""

from gmpy import comb
num = 0
for n in xrange(20,101):
    for r in xrange(1,n):
        if comb(n,r) > 1000000:
            # print n,
            if n%2: more = 2*(n/2 - r +1)
            else: more = 2*(n/2 - r) + 1
            num += more
            break
print num

# one-liner
from gmpy import comb
sum(2*(n/2 -r +1) if n%2  else 2*(n/2 -r)+1 for n in xrange(20,101) for r in xrange(1,n) if comb(n,r) > 1000000)
