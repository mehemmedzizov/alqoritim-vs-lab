def calculate_series_sum(x, epsilon):
    n = 1
    term = x  # İlk hədd x-dir
    total = term

    while abs(term) >= epsilon:
        n += 1
        term = ((-1) ** (n + 1)) * (x ** n) / n
        total += term

    return total


x = 0.5
epsilon = 0.01


result = calculate_series_sum(x, epsilon)
print(f"Cəmin təxmini qiyməti (ε={epsilon} üçün): {result:.4f}")
