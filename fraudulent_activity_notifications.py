# Fraudulent Activity Notifications


def median(expenditures):
    m = len(expenditures) // 2
    if len(expenditures) % 2 != 0:
        mid = expenditures[m]
    else:
        mid = expenditures[m] + expenditures[m - 1]
    return mid

rangeOfInputs = input().split()
days = int(rangeOfInputs[1])
expenditures = list(map(int, input().split()))
spent_day = days
notifications = 0
while spent_day < len(expenditures):
    fraud_days = expenditures[spent_day - days : spent_day]
    fraud_days.sort()
    medianValue = median(fraud_days)
    if expenditures[spent_day] >= medianValue * 2:
        notifications += 1
    spent_day += 1
print(notifications)