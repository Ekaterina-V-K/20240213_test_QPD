def InputNum():
    while True:
        number = input("Введите целое число или 0:")
        try:
            number = int(number)
            break
        except ValueError:
            print("Ошибка: введите корректное число")
    return number


n = InputNum()
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    n=abs(n) #сумму цифр отрицательного числа считаем без учета знака "-"
    while n>0:
        s = s+(n%10)
        n = n//10
    if s > max_s:
        max_s = s
        max_m = m
    n = InputNum()
print('Число',max_m,'имеет максимальную сумму цифр:', max_s)



