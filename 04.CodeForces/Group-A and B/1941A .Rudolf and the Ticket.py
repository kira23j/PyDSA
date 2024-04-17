# Function to count the number of ways Rudolf can select two coins
def count_ways(t, test_cases):
    for test_case in test_cases:
        n, m, k = test_case[0]
        left_coins = test_case[1]
        right_coins = test_case[2]
        
        count = 0
        
        # Loop through all possible combinations of coins
        for i in range(n):
            for j in range(m):
                # If the sum of the denominations is less than or equal to k, increment count
                if left_coins[i] + right_coins[j] <= k:
                    count += 1
        
        print(count)

# Input reading and function call
t = int(input())
test_cases = []

for _ in range(t):
    n, m, k = map(int, input().split())
    left_coins = list(map(int, input().split()))
    right_coins = list(map(int, input().split()))
    test_cases.append([(n, m, k), left_coins, right_coins])

count_ways(t, test_cases)
