def uniq(l):
    uni = []
    uni.append(l[0])
    for i in range(1, len(l)):
        if(uni.count(l[i]) == 0):
            uni.append(l[i])
        
    return uni

print(uniq([1, 2, 3, 4, 5, 3, 5, 3]))
print(uniq([3, 'word', 'f' , 'word', 3 , 2, 4]))