print("Введите число больше 1")
num = int(input())

if num < 1:
    exit

i = 2
while num % i != 0:
    i += 1
    print(f"Число {num} - простое")