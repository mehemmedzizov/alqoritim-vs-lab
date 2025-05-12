def f(x):
    return math.exp(x - 2) * math.log(x + 2)

def simple_iteration(x0, epsilon=1e-6, max_iter=100):
    lambda_val = 0.1
    for i in range(max_iter):
        x1 = x0 - lambda_val * f(x0)
        if abs(x1 - x0) < e
