while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError as e:
        print(f"Ошибка: {e} Введено не число. Попробуйте снова.")
        continue

    op = input("Выберите операцию (+, -, *, /) или 'q' для выхода: ")
    if op.lower() == 'q':
        break
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль невозможно! Попробуйте снова.")
            continue
    else:
        print("Ошибка: Недопустимая Операция! Попробуйте снова.")
        continue

    print(f"Результат: {num1} {op} {num2} = {result}")
