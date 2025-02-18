class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        
        for i, num in enumerate(nums):
            complemento = target - num 
            if complemento in mapa:
                return [mapa[complemento], i]
            mapa[num] = i
            
        return []
    
solution = Solution()

print(solution.twoSum([2,7,11,15], 9))