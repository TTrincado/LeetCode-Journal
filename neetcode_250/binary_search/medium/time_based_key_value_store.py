class TimeMap:
    """
    Logic:
    
    Create a hashmap to map each key with its values and timestamps, and since each
    list is naturally sorted, we can make a binary search in each one.

    Data Structure:
    {
        "key1": [ (val1, time1), (val2, time2), ... ],
        "key2": [ ... ]
    }
    
    Time Complexity: 
      - Set: O(1)
      - Get: O(log N) where N is the number of entries for that specific key.
    Space Complexity: O(Total Entries).
    """
    def __init__(self):
        self.storage = {} # Key -> List of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.storage.get(key, []) # Gets all the values of the keys, if there aren't any, returns []
        l, r = 0, len(values) - 1

        # Look for the exact timestamp or lower
        while l <= r:
            mid = l + (r-l) // 2
            
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res

            elif values[mid][1] < timestamp:
                # Valid candidate, still try to find a closer one
                res = values[mid][0]
                l = mid + 1
            else:
                # Just go left
                r = mid - 1

        return res