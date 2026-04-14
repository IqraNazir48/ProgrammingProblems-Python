def chocolateFeast(n,c,m):
    result=0
    result+=n//c
    wrappers=result
    while(wrappers>=m):
        value=wrappers//m
        another=wrappers%m
        wrappers=value
        result+=wrappers
        wrappers+=another
    return result


# 3       t = 3 (test cases)
# 10 2 5  n = 10, c = 2, m = 5 (first test case)
# 12 4 4  n = 12, c = 4, m = 4 (second test case)
# 6 2 2   n = 6,  c = 2, m = 2 (third test case)
print(chocolateFeast(10,2,5))
print(chocolateFeast(12,4,4))
print(chocolateFeast(6,2,2))