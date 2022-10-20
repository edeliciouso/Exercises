def cash_register(price, cash):
    bills = [100_000, 50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100]
    money = []
    change = cash - price
    x = 0
    while True:
        if x >= 10:
            break
        if change >= bills[x]:
            money.append(bills[x])
            change -= bills[x]
        elif change < bills[x]:
            x += 1
    return money


print(cash_register(75000, 100000))