# Mark and Toys

prices = [1, 12, 5, 111, 200, 1000, 10]
prices.sort()
money = 50
i = 0
total = 0
toys = 0
while i < len(prices):
    if total + prices[i] < money:
        total += prices[i]
        toys += 1
    i += 1
print(toys)