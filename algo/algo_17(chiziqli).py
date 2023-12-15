from math import tan, cos, log, pi
x, y = map(float, input().split())
print("%.2f" % (2*tan(x + pi/6)/(1/3 + pow(cos(y + x**2),2)) + log(x**2 + 2,2)))