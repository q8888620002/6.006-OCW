#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *
from array import array
from timeit import itertools

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.table = {}
        for k , v in pairs:
            self.put(k,v)
            
    # Associates the value v with the key k.
    def put(self, k, v):
        if self.table.has_key(k):
            self.table[k].append(v)
        else:
            self.table[k] = [v]
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        if self.table.has_key(k):
            return self.table[k]
        else:
            return []

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
# param string of seq 
# param number of length
# return k-length subsequence , hash(k- length-seq), index of the start subsequence

def subsequenceHashes(seq, k):
    list_seq = list(seq)   
    split_string = [ [list_seq[i:k+i], i] for i in range(len(list_seq) - k )]
    for i in split_string:
        hash = RollingHash(i[0]).current_hash()
        yield hash, i[1]
        
        
# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    seq_b = list(subsequenceHashes(b, k))
    data = Multidict(subsequenceHashes(a, k))

    for hash_b , index_b in seq_b:
        if data.get(hash_b):
            for index_a in data.get(hash_b):
                yield (index_a , index_b)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
