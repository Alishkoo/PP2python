def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    if(numheads < numlegs and numlegs % 2 == 0):
        rabbit = (numlegs - 2 * numheads) / 2
        chicken = numheads - rabbit
    else:
        print('Error')
    return [int(chicken), int(rabbit)]

print(solve(35,94))
    