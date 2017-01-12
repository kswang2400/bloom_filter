class BloomFilter(object):
    def __init__(self):
        self.space = {}

    def add(self, element):
        self.space[hash1(element)] = True
        self.space[hash2(element)] = True
        self.space[hash3(element)] = True

        return True

    def has(self, element):
        return (
            hash1(element) in self.space
                or hash2(element) in self.space
                or hash3(element) in self.space
            )

def hash1(element):
    return hash(element)

def hash2(element):
    return hash(element) + 10

def hash3(element):
    return hash(element) + 100