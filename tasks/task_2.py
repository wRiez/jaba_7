n_one = int(input())
n_two = int(input())
n_three = int(input())

if (n_one > n_two) and (n_one > n_three):
    print(f"{n_one} - большее число")
elif (n_two > n_one) and (n_two > n_three):
    print(f"{n_two} - большее число")
elif (n_three > n_one) and (n_three > n_two):
    print(f"{n_three} - большее число")