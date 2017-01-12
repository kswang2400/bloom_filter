class BloomFilter(object):
    def __init__(self, depth=3, size=10 ** 7):
        self.depth  = depth
        self.size   = size
        self.space  = [None] * self.size

    def _hash(self, element):
        index = hash(element) % self.size

        return index


    def add(self, element):
        for _ in xrange(self.depth):
            index = self._hash(element)
            self.space[index] = True
            element = index

        return True

    def has(self, element):
        for _ in xrange(self.depth):
            index = self._hash(element)
            if self.space[index]:
                return True

            element = index

        return False