def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            test, nums = line.strip().split(":")
            test = int(test.strip())
            nums = list(map(int, nums.strip().split()))
            res.append([test, nums])
    return res


file_path = "./inputs/07.txt"
inputs = read_input(file_path)


def is_calibrated(test, nums, curr, i):
    if i == len(nums):
        return curr == test
    if curr > test:
        return False
    if is_calibrated(test, nums, curr + nums[i], i + 1):
        return True
    if is_calibrated(test, nums, curr * nums[i], i + 1):
        return True


calibration = 0
for test, nums in inputs:
    if is_calibrated(test, nums, 0, 0):
        calibration += test

print(calibration)
