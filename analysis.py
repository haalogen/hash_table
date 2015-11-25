import sys
import numpy as np
import func as fu
import matplotlib.pyplot as plt

# default parameters
N = 113  # size of HashTable
TIMES = 1 # num of experiments for averaging


if len(sys.argv) >= 2:
    N = int(sys.argv[1])

if len(sys.argv) >= 3:
    TIMES = int(sys.argv[2])


collis_hl_cnt = np.zeros(N)
collis_hq_cnt = np.zeros(N)


for t in xrange(TIMES):
    
    # fill the hash table
    q_probe = False
    hl = fu.HashTable(q_probe, N)
    
    q_probe = True
    hq = fu.HashTable(q_probe, N)
    
    for i in xrange(N):
        n_key = np.random.rand()
        print n_key
        collis_hl_cnt[i] += hl.put(n_key)
        collis_hq_cnt[i] += hq.put(n_key)
    
    print sorted(hl.slots)
    print sorted(hq.slots)
    
    if any(x is None for x in hl.slots):
        print 'WTF, linear probing???'
        
    if any(x is None for x in hq.slots):
        print 'Quadratic probing didn\'t fill the HashTable!!!'

collis_hl_cnt /= TIMES
collis_hq_cnt /= TIMES

print 'Collisions, linear probe: \n', collis_hl_cnt
print 'Collisions, quadratic probe: \n', collis_hq_cnt

alpha = np.arange(1.0, float(N+1)) / N
print alpha

lbl = 'Linear probing'
plt.plot(alpha, collis_hl_cnt, label=lbl)
lbl = 'Quadratic probing'
plt.plot(alpha, collis_hq_cnt, label=lbl)

title = 'Collision analysis in HashTable: Linear vs Quadratic probing. '
title += "N = %r; TIMES = %r" % (N, TIMES)
plt.title(title)
plt.xlabel(r"$\alpha = i / N$ -- ('density' coefficient)")
plt.ylabel('AVERAGE Number of collisions')

plt.legend(loc=2)
plt.show()


