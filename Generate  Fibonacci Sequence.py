# The Fibonacci sequence is the integer sequence of 0,1,1,2,3,5,8,......

# The first two terms are 0 and 1. All other terms are obtained by adding the two preceding terms.

# This means to say the nth term is equal to (n-1)th+(n-2)th term.

n_terms = 10

# first two terms
n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence upto,"n_terms,":" )
while count < n_terms:
    print(n1, end=',')
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth 
    count += 1
print()
