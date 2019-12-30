nums = input("Enter your nums: ").split(' ')
for x in nums:
    if int(x) % 2 == 0:
        print(x)
    else:
        continue