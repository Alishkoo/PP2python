nums = input().split(' ')

def prime():
    another = []
    global nums
    for i in range(0, len(nums)):
        if(int(nums[i]) % 2 == 1):
            another.append(nums[i])

    return another

print(prime())

