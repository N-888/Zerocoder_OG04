while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError as e:
        print(f"Ошибка: {e} Введено не число. Попробуйте снова.")
        continue

