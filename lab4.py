import random

n = 10 
A = [random.randint(1, 100) for _ in range(n)]

with open("massiv.txt", "w") as f:
    f.write(" ".join(map(str, A)))


with open("massiv.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
    odd_numbers = [num for num in numbers if num % 2 != 0]  

odd_sum = sum(odd_numbers) 
with open("tek_ededler.txt", "w") as f:
    f.write(" ".join(map(str, odd_numbers)))


print(f"Tək ədədlər: {odd_numbers}")
print(f"Tək ədədlərin cəmi: {odd_sum}")
