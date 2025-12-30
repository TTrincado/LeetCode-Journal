class MyHashSet:
    '''
    First Approach: Brute Force with manual iteration.

    O(n) time complexity for each operation, as well as O(n) for storage.
    '''

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        for index, elem in enumerate(self.set):
            if key == elem:
                return
        self.set.append(key)

    def remove(self, key: int) -> None:
        for index, elem in enumerate(self.set):
            if key == elem:
                self.set.pop(index)

    def contains(self, key: int) -> bool:
        for index, elem in enumerate(self.set):
            if key == elem:
                return True
        return False

    # O(n) for each operation, both time and space.


class MyHashSet2:
    '''
    Brute Force using Python's in / not in operations.
    (Same complexity, shorter code)
    '''

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.set


class MyHashSet3:
    """
    Uses the array indexes of a boolean array to represent the number.

    Super clever way to have O(1) time operations, at the expense of having
    O(m) space where m is the size of the boolean array.
    """

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
