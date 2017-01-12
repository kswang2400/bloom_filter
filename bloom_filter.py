class BloomFilter(object):
    def __init__(self):
        self.space = [None] * 10 ** 7

    def add(self, element):
        self.space[hash1(element)] = True
        self.space[hash2(element)] = True
        self.space[hash3(element)] = True

        return True

    def has(self, element):
        return (
            self.space[hash1(element)]
            or self.space[hash2(element)]
            or self.space[hash3(element)]
        )

def hash1(element):
    return hash(element) % 10 ** 7

def hash2(element):
    return hash(element) % 10 ** 7 + 10

def hash3(element):
    return hash(element) % 10 ** 7 + 1000