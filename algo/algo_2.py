from math import pi
a, b, c = map(int, input().split())
s1, s2, s3 = pi*a*a, pi*b*b, pi*c*c
print("%.2f" % s1, "%.2f" % s2, "%.2f" % s3)