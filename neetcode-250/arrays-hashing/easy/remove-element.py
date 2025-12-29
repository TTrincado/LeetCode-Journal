class Solution:
    '''
    Instructions and notes were kinda hard to understand imo.

    Basically, just track the values =! to target and swap them to the beggining of the list. 

    After the k elements, the list can contain whatever.

    A good takeaway is to avoid mutating a list's structure while iterating in it. 
    Modifying or swapping values will work just fine as long as you keep track of the pointers.
    '''

    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
