# step one:recursive case
def fibbon(n):
    # step3: validate inputs
    assert n>=0 and int(n)==n,'must be int and positive'
    # step2:base case-stop condition
    if n in [0,1]:
        return n
    else:
        return fibbon(n-1)+fibbon(n-2)
print(fibbon(4))