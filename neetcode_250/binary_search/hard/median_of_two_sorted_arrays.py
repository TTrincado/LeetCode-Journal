class Solution:
    """
    Logic:
    We try to find a cut in both arrays such that:
    1. The left partition contains (Total + 1) // 2 elements.
    2. All elements on the left are <= All elements on the right.


    If we cut Array A at index 'i', we MUST cut Array B at index 'j' such that:
    i + j = (len(A) + len(B) + 1) // 2.

    Binary Search:
    We perform BS on the cut position 'i' of the SMALLER array (to minimize complexity).
    - If A_left > B_right: We took too much from A. Move cut Left.
    - If B_left > A_right: We took too little from A. Move cut Right.

    Time Complexity: O(log(min(N, M)))
    Space Complexity: O(1)
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        
        # The +1 ensures the Left Partition holds the extra element (the median) 
        # if Total length is Odd.
        half = (total + 1) // 2

        # Always BS on the smaller array to guarantee O(log(min(N,M)))
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2  # Cut in A
            j = half - i      # Cut in B (Dependent on A)

            # These handle the edge cases, if we have in a partition all of A or B,
            # we can't compare the numbers correctly below, but we know the condition
            # should pass so we use float(-/+inf) so in these cases they always pass
            A_left = A[i - 1] if i > 0 else float("-inf")
            B_left = B[j - 1] if j > 0 else float("-inf")

            A_right = A[i] if i < len(A) else float("inf")
            B_right = B[j] if j < len(B) else float("inf")

            # We compare the four numbers in between the partitions to check if its the median.
            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    # Odd total: The median is the max of the left side
                    return max(A_left, B_left)
                else:
                    # Even total: Average of max(left) and min(right)
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                # Reduce A's partition size.
                r = i - 1
            else:
                # (B_left > A_right). Increase A's partition.
                l = i + 1

# NOTE The binary search should be performed on the smaller array to ensure the partition index
# in the larger array stays within bounds. If you search on the larger array, the computed index
# j = half - i for the smaller array may become negative or exceed its length, causing index-out-of-bounds errors.
