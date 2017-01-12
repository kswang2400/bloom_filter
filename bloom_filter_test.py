import unittest
import string
import random

from .bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter()
        self.test_length = 1000
        self.element_length = 10

    def test_add(self):
        assert self.bf.add(create_random_string(self.element_length))


    def test_basic_add_check(self):
        positives = []
        for _ in xrange(self.test_length):
            positives.append(create_random_string(self.element_length))

        negatives = []
        for _ in xrange(self.test_length):
            negatives.append(create_random_string(self.element_length))


        for e in positives:
            self.bf.add(e)
            assert self.bf.has(e)

        print "{count} positives assertions true".format(count=len(positives))

        for e in negatives:
            assert not self.bf.has(e)

        print "{count} negatives assertions true".format(count=len(negatives))

def create_random_string(length):
    s = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits
        ) for _ in xrange(length)
    )

    return s