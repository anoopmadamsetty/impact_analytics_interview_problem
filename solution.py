"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or
reduce the fraction to decimal

Test cases:
for 5 days: 14/29
for 10 days: 372/773

"""


def is_valid(s):
    """Validate string only if maximum consecutive 0's are
    less than or equal to 3."""
    # find max consecutive 0s
    c = 0
    maxCount = 0
    for char in s:
        if char == '0':
            c += 1
        if char == '1':
            maxCount = max(maxCount, c)
            c = 0
        maxCount = max(maxCount, c)
    return maxCount <= 3


def prob_absent_and_allowed(n):
    """Returns 'Answer of (2) / Answer of (1)'."""
    allowed = 0
    not_allowed = 0
    absent_at_graduation = 0
    for i in range(2**n):
        b = '{:0{}b}'.format(i, n)
        if is_valid(b):
            if b[-1] == '0':
                absent_at_graduation += 1
            allowed += 1
        else:
            not_allowed += 1
    return str(absent_at_graduation) + "/" + str(allowed) + " / " + str(allowed)


if __name__ == "__main__":

    print(prob_absent_and_allowed(5))

    print("######")

    print(prob_absent_and_allowed(10))
