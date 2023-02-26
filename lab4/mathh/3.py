import math as m

def area_reg(n, a):
    up = (n * pow(a,2))
    down = (4 * m.tan(m.pi / n))
    return up / down

print(area_reg(4, 25))