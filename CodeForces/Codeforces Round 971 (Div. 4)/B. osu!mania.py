def osu_mania(t, test_cases):
    results = []
    for case in test_cases:
        n, beatmap = case
        columns = []
        for row in beatmap:
            for j in range(4):
                if row[j] == '#':
                    columns.append(j + 1)  # Convert 0-based index to 1-based
                    break
        results.append(" ".join(map(str, columns[::-1])))  # Reverse the list before output
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    beatmap = [input().strip() for _ in range(n)]
    test_cases.append((n, beatmap))

# Process and get results
results = osu_mania(t, test_cases)

# Output results
for result in results:
    print(result)
