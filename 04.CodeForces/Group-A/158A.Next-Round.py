def advance_to_next_round(n, k, scores):
    kth_place_score = scores[k-1]
    
    # Count the number of participants with a score greater than or equal to kth place
    count_advancers = sum(score >= kth_place_score and score > 0 for score in scores)
    
    return count_advancers

# Read input
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Calculate and print the result
result = advance_to_next_round(n, k, scores)
print(result)
