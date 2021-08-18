days_campaign = int(input())
bak_campaign = int(input())
cake_baker_day = int(input())
gauf_baker_day = int(input())
pancake_baker_day = int(input())
Total = (cake_baker_day * 45 + gauf_baker_day * 5.80 + pancake_baker_day * 3.20)
total_amount  = Total * bak_campaign * days_campaign
Profit = total_amount- 1 / 8 * total_amount
print(Profit)
