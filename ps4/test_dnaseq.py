from dnaseq import *
import unittest
from wheel.signatures import assertTrue

### Testing ###

#Test the test subsequencehash 
class TestSubsequenceHash(unittest.TestCase):
    def test_hash(self):
        h1 = subsequenceHashes(iter('TATAAUTCG'), 4)
        #for i, h , j in h1:
         #   print i, h ,j
            
class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('CTAGC')
        rh2 = RollingHash('TAGCG')
        rh3 = RollingHash('AGCGT')
        rh1.slide('C','G')
        self.assertTrue(rh1.current_hash() == rh2.current_hash())
        rh1.slide('T','T')
        self.assertTrue(rh1.current_hash() == rh3.current_hash())

# Test Multidict initialization 
class TestMultidict1(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# Test Multidict initialization 
class TestMultidict2(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        foo.put(2, 'e')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b','e'])
        self.assertTrue(foo.get(3) == [])
        
# This test case may break once you add the argument m (skipping).
class TestExactSubmatches(unittest.TestCase):
   def test_one(self):
       foo = 'yabcabcabcz'
       bar = 'xxabcxxxx'
       matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 1))
       print matches
       correct = [(1,2), (4,2), (7,2)]
       self.assertTrue(len(matches) == len(correct))
       for x in correct:
           self.assertTrue(x in matches)

class TestIntervalsub(unittest.TestCase):
    def test_one(self):
        foo = 'absdfasdfasdf'
        result = ['abs','asd','sdf']
        assertTrue(intervalSubsequenceHashes(foo,3 , 5), result)

unittest.main()
