nums = [1, 2, 3, 4, 5, 6, 7]
type(nums)
sum = 0
prod = 1
for x in nums:
    sum += x
    prod *= x
print('sum = ', sum)
print('product = ', prod)
