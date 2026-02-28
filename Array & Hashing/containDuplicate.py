class Solution:
    def containsDuplicate(self, nums) -> bool:
        b = sorted(nums)
        for i in range(len(b) - 1):
            if b[i] == b[i+1]:
                return True
        return False
                
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))