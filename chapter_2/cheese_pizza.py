unit = int(input())
extra = int(input())

if unit == 3 and extra >= 95:
    feeling = 'absolutely'
elif (unit == 1 and extra <= 50):
    feeling = 'fairly'
else:
    feeling = 'very'


print('C.C. is', feeling, 'satisfied with her pizza.')