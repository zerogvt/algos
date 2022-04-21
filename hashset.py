class MyHashSet:

    def __init__(self):
        self.bitarray = 1<<(10**6) 

    def add(self, key: int) -> None:
        self.bitarray = self.bitarray | (1<<key)

    def remove(self, key: int) -> None:
        self.bitarray = self.bitarray & ~(1<<key)

    def contains(self, key: int) -> bool:
        return self.bitarray & (1<<key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
