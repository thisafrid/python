nums = [2,4,5,66,7,999,32,53,32]

x = 999
i = 0
while i < len(nums):
    if nums[i] == x:
        print("found", i)
    else:
        print("searching.")
        i+=1
