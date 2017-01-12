class BloomFilter(object):
    __slots__ = tuple('a' + str(i) for i in xrange(10 ** 7))

    def add(self, element):
        setattr(self, 'a' + str(hash1(element)), True)
        setattr(self, 'a' + str(hash2(element)), True)
        setattr(self, 'a' + str(hash3(element)), True)

        return True

    def has(self, element):
        try:
            return getattr(self, 'a' + str(hash1(element)))
            return getattr(self, 'a' + str(hash2(element)))
            return getattr(self, 'a' + str(hash3(element)))
        except AttributeError:
            pass

        return False

def hash1(element):
    return hash(element) % 10 ** 7

def hash2(element):
    return hash(element) % 10 ** 7 + 10

def hash3(element):
    return hash(element) % 10 ** 7 + 1000