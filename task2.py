num = int(input("Введите время в секундах: "))
minutes = float(num / 60)
hours = float(num / 3600)
print(f"Время в формате: ч:м:с    {hours}: {minutes}: {num}")
