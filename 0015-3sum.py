# 15. 3Sum
# https://leetcode.com/problems/3sum/
#
# Idea: как в 2sum, но здесь таргетом выступает наш нынешний -nums[i]
# Time: O(n^2)   Space: O(n)


class Solution:
#Верное решение - но тайм exceeded, O(n^3) из-за тройного вложения. хотя все равно меньше, чем это
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     triples = []
    #     for i in range(len(nums)-2):
    #         for j in range(i+1, len(nums)-1):
    #             for k in range(j+1, len(nums)):
    #                 if nums[i]+nums[j]+nums[k] == 0:
    #                     triple = [nums[i],nums[j],nums[k]]
    #                     triple.sort()
    #                     if triple not in triples:
    #                         triples.append(triple)
    #     return triples
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     nums.sort()
    #     targets = {}
    #     amounts = {}
    #     answer = []
    #     amounts[nums[len(nums)-1]] = 1
    #     for i in range(len(nums)-1):
    #         if nums[i] not in amounts:
    #             amounts[nums[i]] = 0
    #         amounts[nums[i]] += 1
    #         if i >= 1 and nums[i]== nums[i-1]:
    #             continue
    #         for j in range(i+1,len(nums)):
    #             target = -nums[i]-nums[j]
    #             is_new = True
    #             if target not in targets:
    #                 targets[target] = []
    #             elif target in targets:
    #                 for pair in targets[target]:
    #                     if pair == [nums[i], nums[j]]:
    #                         is_new = False                                                          
    #                         break
    #             if is_new:
    #                 targets[target].append([nums[i],nums[j]])
    #     for value in amounts:
    #         if value in targets:
    #             for pair in targets[value]:
    #                 if value == pair[0] and value == pair[1] and amounts[value]<3:
    #                     continue
    #                 elif  (value == pair[0] and value != pair[1]) or  (value != pair[0] and value == pair[1]) and amounts[value] < 2:
    #                     continue
    #                 pair.append(value)
    #                 triple = sorted(pair)
    #                 if triple not in answer:
    #                     answer.append(triple)
    #     return answer

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triples = []
        for i in range(len(nums)-2):
            
            left = i+1
            right = len(nums)-1
            target = 0-nums[i]
            if i>=1 and nums[i]==nums[i-1]:
                continue
            while left < right:
                if nums[left] + nums[right] == target:
                    triples.append([nums[i],nums[left], nums[right]]) 
                elif nums[left] + nums[right] > target:
                    right -= 1
                    continue
                left += 1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left += 1
        return triples

print(Solution().threeSum([-1,0,1,2,-1,-4]))  # expected [[-1, -1, 2], [-1, 0, 1]] (any order)
print(Solution().threeSum([0, 1, 1])) 
print(Solution().threeSum([0, 0, 0])) 
print(Solution().threeSum([0, 0, 0, 0])) 

