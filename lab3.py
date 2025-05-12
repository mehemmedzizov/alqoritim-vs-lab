
n = 3  
m = 4  

import random
A = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]


print("Massiv A:")
for row in A:
    print(row)


row_sums = []
for i in range(n):
    row_sum = sum(A[i])  
    row_sums.append(row_sum)
    print(f"Sətrin {i+1} cəmi: {row_sum}")

