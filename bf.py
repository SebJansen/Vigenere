import math
import time
from typing import List

# nums: List[int] = [MIN, MIN, MIN]
# END = len(nums) - 1
#
# hold: int = 0
# move: int = len(nums) - 1
#
# iteration = 1
#
# nums_index = 0

# while nums_index < len(nums):
    # print(nums)
    # time.sleep(1)
    # # print(nums[nums_index])
    # # print(2 ** nums_index)
    #
    # if (((nums[nums_index] + 1) % (2 ** (nums_index)))) == 0:
    #     nums_index += 1
    # else:
    #     nums[nums_index] += 1

DIGIT_MIN: int = 97
DIGIT_MAX: int = 99
DIGIT_AMOUNT: int = 6
limit = DIGIT_MAX + 1
i = 0
combinations = (limit ** DIGIT_AMOUNT) - 1


while i < combinations:
    n = i
    i += 1
    numbers = [math.floor(i / ((DIGIT_MAX + 1) ** n)) % (DIGIT_MAX + 1) for n in range(0, DIGIT_AMOUNT)]
    print(numbers)
    time.sleep(1)
