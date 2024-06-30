burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1:
    burger_calorie = 461
elif burger == 2:
    burger_calorie = 431
elif burger == 3:
    burger_calorie = 420
else:
    burger_calorie = 0

if side == 1:
    side_calorie = 100
elif side == 2:
    side_calorie = 57
elif side == 3:
    side_calorie = 70
else:
    side_calorie = 0

if drink == 1:
    drink_calorie = 130
elif drink == 2:
    drink_calorie = 160
elif drink == 3:
    drink_calorie = 118
else:
    drink_calorie = 0

if dessert == 1:
    dessert_calorie = 167
elif dessert == 2:
    dessert_calorie = 266
elif dessert == 3:
    dessert_calorie = 75
else:
    dessert_calorie = 0

calorie_total = burger_calorie + side_calorie + drink_calorie + dessert_calorie
print('Your total Calorie count is ' + str(calorie_total) +'.')