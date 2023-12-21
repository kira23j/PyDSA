# even if we can increase stack memory the function keeps call
# calling itself infintely
# import sys
# sys.setrecursionlimit()
# step one:recursive case the flow
# step2:base case the stopping criteria
# step3:unintentional case-constraint
def factorial(n):
    # for step 3
    assert n>=0 and int(n)==n,'the number must be positive integer only'
    #  for step 1
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
num=int(input("please enter a number: "))
print(f"the factorial of {num} is: {factorial(num)}")