print("Введите целое неотрицательное число")
num = int(input())

if num < 0:
    exit
j = 1
i = 2
while i <= num:
    j = j * i
    i = i + 1
    print(j)
print(f"Факториал {num} - {j}")