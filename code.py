# Why do we need to test prospective merges?
""" 
Let's say my goal is two things:
1. Print x from 1 to 10.
2. Empty x.

The initial commit is going to miss part of #1 and #2.
"""
x = []

def printOneToTenThenDelete():
    x += [1,2,3]
    


    x += [4,5,6]
    


    x += [7,8,9,10]
    

    print(x)    
    return x

result = printOneToThenThenDelete()
assert len(result) == 0