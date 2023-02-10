nums = input().split(' ')

def prime():
    cnt = 0
    another = []
    global nums
    for i in range(0, len(nums)):
        for j in range(1, int(nums[i]) + 1):
            if(int(nums[i]) % j == 0):
                cnt+=1
        if(cnt == 2):
            another.append(nums[i])
        cnt = 0
            

            

    return another

print(prime())

