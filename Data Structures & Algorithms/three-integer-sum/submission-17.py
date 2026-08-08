class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:



        def twosumhelper(end, target):
            i = 0
            pairs = defaultdict(list)
            res = []
            while i < end:
                    
                if target - nums[i] in pairs:
                    res.append((nums[i], nums[pairs[target - nums[i]]]))

                pairs[nums[i]] = i
                i += 1

            return res

        nums.sort()


        triplets = set()
        for i in range(len(nums)):


            target = -nums[i]
            pairs = twosumhelper(i, target)

            for pair in pairs:
                triplets.add((pair[0], pair[1], nums[i]))

        return list(triplets)






        