from typing import List


class Solution:
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        # sort the array
        nums.sort()
        
        # container for result
        triplets: List[List[int]] = []
        
        # consoder every number as X
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # find two numbers which adds up to -X
            self.find_two_sum(nums, -nums[i], i+1, triplets)
            
        return triplets
    
    
    def find_two_sum(self, nums: List[int], target_sum: int, left: int, triplets:List[List[int]]):
        
        right = len(nums) - 1
        
        while left < right:
            
            current_sum = nums[left] + nums[right]
            
            if current_sum == target_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                
                # avoid duplicates
                while left < right and left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1

                # avoid duplicates
                while left < right and right > 0 and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif current_sum > target_sum:
                right -= 1
            elif current_sum < target_sum:
                left += 1
            
# x + Y + Z = 0
# Y + Z = -X
                
            
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))