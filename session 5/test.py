#stock and price
total=0
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    total=total+prices[key]*stock[key]
    print(key)
    print('prices: ',prices[key])
    print('stock: ',stock[key])
    print()
print(total)