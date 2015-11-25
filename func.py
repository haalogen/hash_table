"""Basic functionality of the project "Hash_Table"."""
def float2hash(f):
    """Float value to hash (int)"""
    s = str(f)
    
    n_hash = 0
    for ch in s:
        if ch.isdigit():
            n_hash = (n_hash << 5) + n_hash + ord(ch)
#            print ch, n_hash
    
    
    return n_hash



class HashTable(object):
    def __init__(self, q_probe=False , sz=101):
        self.size = sz
        self.slots = [None] * self.size
        # False <-> linear probing
        # True <-> quadratic probing
        self.quad_probe = q_probe
    
    
    def __repr__(self):
        return str(self.slots)
    
    
    def hash_function(self, key):
        return float2hash(key) % self.size
    
    
    
    def rehash(self, oldhash, iteration):
        n_hash = 0
        
        if self.quad_probe:
            # do quadratic probing rehash
            n_hash = (oldhash + iteration**2) % self.size
            print 'rehash_qua:', n_hash
            
        else:
            # do linear probing rehash
            n_hash = (oldhash + iteration) % self.size
            print 'rehash_lin: ', n_hash
        
#        raw_input()
        return n_hash
    
    
    def put(self, key):
        collis_cnt = 0
        hashvalue = self.hash_function(key)
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            
        else:
            if self.slots[hashvalue] == key:
                pass # do nothing
            else:
                iter_cnt = 1
                first_hash = hashvalue
                nextslot = self.rehash(first_hash, iter_cnt)
                
                # looking for our key or empty slot
                while self.slots[nextslot] != None and \
                    self.slots[nextslot] != key and iter_cnt <= self.size:
                    iter_cnt += 1
                    nextslot = self.rehash(first_hash, iter_cnt)
                
                collis_cnt = iter_cnt
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    
                # else <-> self.slots[nextslot] == key => do nothing
        return collis_cnt
    
