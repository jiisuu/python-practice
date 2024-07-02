a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a > c and a < b):
    mama_bear_weight = a
elif (b > a and b < c) or (b > c and b < a):
    mama_bear_weight = b
else:
    mama_bear_weight = c

print(mama_bear_weight)