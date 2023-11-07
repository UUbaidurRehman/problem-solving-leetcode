class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l ,r = 0 , len(nums)-1
        if r== 0:
            return nums[r]
        while l < r :
            mid = l + (r-l)//2
            if (mid % 2 == 0 and nums[mid]==nums[mid+1]) or \
                (mid % 2 ==1 and nums[mid] == nums[mid-1]):
                    l = mid+1
            elif ((mid % 2 == 0 and nums[mid] == nums[mid-1]) or 
            (mid % 2 ==1 and nums[mid]== nums[mid+1])):
                    r = mid
            else:
                return nums[mid]
        return nums[l]

        



        





        # l,r = 0, len(nums)
        # if len(nums) <=1:
        #     return nums[r-1]
        # while (l < r):
        #     mid = l + (r-l)//2
        #     if mid % 2 == 0:
        #         if nums[mid] == nums[mid-1]:
        #             r = mid
        #         elif nums[mid] == nums[mid+1]:
        #             l = mid+1
        #         else:
        #             return nums[mid]

        #     else:
        #         if nums[mid] == nums[mid-1]:
        #             l = mid+1
        #         elif nums[mid] == nums[mid+1]:
        #             r = mid
        #         else:
        #             return nums[mid]
        # return mid