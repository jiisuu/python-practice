month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special")
elif (month == 1 and day <= 31) or (month == 2 and day < 18) :
    print("Before")
elif (month == 2 and 18 < day <= 31) or (month > 2 and day <= 31):
    print("After")