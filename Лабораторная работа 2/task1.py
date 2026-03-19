money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
m=1 #Переменная для рассчета количества месяцев
money_capital = money_capital - spend + salary #Рассчет бюджета посте первого месяца трат

while money_capital+salary>=spend:   #Цикл для проверки заданного условия
    spend= spend*(1+increase)
    money_capital = money_capital - spend + salary
    m+=1                            #Увеличиваем номер месяца после каждой операции

print("Количество месяцев, которое можно протянуть без долгов:", m)  #Вывод ответа
