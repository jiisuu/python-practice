P = int(input())
C = int(input())
M = int(input())

badges = P // C
badge_sales = badges * M
leftover_paint = P % C
leftover_sales = leftover_paint * 1
total_money = badge_sales + leftover_sales

print(total_money)
