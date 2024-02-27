def can_divide_watermelon(w):
    return "YES" if w > 2 and w % 2 == 0 else "NO"

# Read input
w = int(input())

# Output result
print(can_divide_watermelon(w))
