class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i, n in enumerate(nums):
            if n != 0:
                continue

            # Swap the zero with the next available int.
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                break


