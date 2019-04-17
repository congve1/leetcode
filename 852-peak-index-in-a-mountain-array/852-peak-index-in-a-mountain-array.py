class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                return i
        """
        left = 1 
        right = len(A)-2
        while left <= right:
            mid = (left+right)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid+1] and A[mid] > A[mid-1]:
                left = mid + 1
            elif A[mid] > A[mid+1] and A[mid] < A[mid-1]:
                right = mid - 1
        return -1