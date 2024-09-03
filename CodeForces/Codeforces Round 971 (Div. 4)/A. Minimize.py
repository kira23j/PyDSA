def minimize_expression(t, test_cases):
    results = []
    for a, b in test_cases:
        c = (a + b) // 2  # The midpoint value of a and b
        result = (c - a) + (b - c)  # Which is always equal to b - a
        results.append(result)
    return results

# Reading input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = minimize_expression(t, test_cases)

# Output results
for res in results:
    print(res)
