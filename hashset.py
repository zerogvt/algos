# HashSet implementation with a bitmap
# Can host integer values [1, 10**6]

class VHashSet:
    def __init__(self):
        self.hs = 1 << (10**6+1)

    def insert(self, key: int) -> 'VHashSet':
        self.hs |= 1 << key
        return self
    
    def delete(self, key: int) -> 'VHashSet':
        self.hs &= ~(1<<key)
        return self

    def contains(self, key: int) -> bool:
        return bool(self.hs & (1<<key))

vhs = VHashSet()
vhs.insert(1).insert(2).insert(10**6)
print(vhs.contains(1))
print(vhs.contains(10**6))
vhs.delete(1)
print(vhs.contains(1))
