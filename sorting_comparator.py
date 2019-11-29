# Sorting: Comparator

players = [['amy', 100], ['david', 100], ['heraldo', 50], ['aakansha', 75], ['aleksa', 150]]
players.sort()
players.sort(key=lambda x:x[1],reverse=True)
print(players)