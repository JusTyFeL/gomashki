#задач 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(a+b)

#задач 2
def count_trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

n = int(input("Введите число : "))
factorial_zeros = count_trailing_zeros(n)
print(f"Количество нулей в конце факториала {n} равно {factorial_zeros}")