'''Search for a number x in this tuple using loop:
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0

for val in nums:
    if val == x:
        print("found at", idx)
        break
    idx += 1
else:
    print("not found")
