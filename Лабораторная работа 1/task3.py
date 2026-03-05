list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Находим номер середины списка
ind = len(list_players) // 2

first = list_players[:ind] #Список первой половины изначального списка
second = list_players[ind:] #Список второй половины изначального списка

print(first)
print(second)
