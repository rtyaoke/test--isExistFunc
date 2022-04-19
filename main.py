import timeit

"""
線形探索のテスト

結論）
・特定値の存在確認はforin[is_exist_target_v1()]が3倍ぐらい速い
  -> pythonは代入・比較の処理コストが高い（処理前に型調査発生）
・特定値のインデックス取得はforin[index_of_target_v1()]がわずかに速い(ほぼ誤差)
"""


def is_exist_target_v1(nums: list, target: int):
    for num in nums:
        if num == target:
            return True
    return False


def is_exist_target_v2(nums: list, target: int):
    i = 0
    n = len(nums)
    while i < n and nums[i] != target:
        i += 1
    return i < n


def is_exist_target_v3(nums: list, target: int):
    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False


def is_exist_target_v4(nums: list, target: int):
    n = len(nums)
    new_nums = nums + [target]
    i = 0
    while new_nums[i] != target:
        i += 1
    return i != n


def index_of_target_v1(nums: list, target: int):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def index_of_target_v2(nums: list, target: int):
    nums.append(target)
    i = 0
    while nums[i] != target:
        i += 1
    if i != len(nums):
        return -1
    else:
        return i


def measure_time(fn_name, fn):
    print(fn_name, len(nums), fn(nums, target))
    print(fn_name, timeit.timeit(f'{fn_name}(nums, target)',
          globals=globals(), number=100))


nums = list(range(100000))
target = 100000

measure_time('is_exist_target_v1', is_exist_target_v1)
measure_time('is_exist_target_v2', is_exist_target_v2)
measure_time('is_exist_target_v3', is_exist_target_v3)
measure_time('is_exist_target_v4', is_exist_target_v4)

measure_time('index_of_target_v1', index_of_target_v1)
measure_time('index_of_target_v2', index_of_target_v2)
