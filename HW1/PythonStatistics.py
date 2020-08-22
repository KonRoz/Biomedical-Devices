from statistics import mean, pstdev

def average(nums):
    total = 0
    for ele in nums:
        total += ele

    return total / len(nums)

def ele_squared(nums):
    total = 0
    for ele in nums:
        total += ele**2

    return total / len(nums)

def std_dev(nums):
    diff = ele_squared(nums) - average(nums)**2
    return diff**0.5

print("\n\n\t\t\tPython Statistics\n\n")

x1 = [1,2,3,4]
x2 = [1,4,9,16]

print("Set 1: %s, Set 2: %s" % (str(x1), str(x2)))

my_avg1 = average(x1)
my_avg2 = average(x2)
py_avg1 = mean(x1)
py_avg2 = mean(x2)

print("\n\n\tSet 1:\n\t\t My Mean: %s, Statistics Mean: %s" % (str(my_avg1), str(py_avg1)))
print("\n\n\tSet 2:\n\t\t My Mean: %s, Statistics Mean: %s" % (str(my_avg2), str(py_avg2)))

my_dev1 = std_dev(x1)
my_dev2 = std_dev(x2)
py_dev1 = pstdev(x1)
py_dev2 = pstdev(x2)

print("\n\n\tSet 1:\n\t\t My Deviation: %s, Statistics Deviation: %s" % (str(my_dev1), str(py_dev1)))
print("\n\n\tSet 2:\n\t\t My Deviation: %s, Statistics Deviation: %s" % (str(my_dev2), str(py_dev2)))
