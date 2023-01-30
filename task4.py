costs = int(input("Введите затраты предприятия: "))
profit = int(input("Введите выручку предприятия: "))
if profit>costs:
    profitability=float(profit/costs)
    print(f"Предприятие получило прибыло: {profit-costs}")
    print(f"Рентабельность предприятия: {round(profitability,2)}")
    staff = int(input("Введите количество сотрудников "))
    profit_staff = float(profit/staff)
    print(f"Прибыль на одного сотрудника составляет: {round(profit_staff,2)}")
else:
    print("Предприятие не рентабельное")