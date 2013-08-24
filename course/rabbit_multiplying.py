# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

#def rabbits(n):
#    if n == 1 or n == 2:
#        return 1
#    elif n >=3 and n <= 5:
#        return rabbits(n - 1) + rabbits(n - 2)
#    else:
#        return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
#
#
#
#print rabbits(10)
##>>> 35
#s = ""
#for i in range(1,12):
#    s = s + str(rabbits(i)) + " "
#print s
##>>> 1 1 2 3 5 7 11 16 24 35 52

# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math. 

def hexes_to_udaciousness(n, spread, target):
    base = n + n * spread
    if base >= target:
        yield count
    else:
        count = count + 1
        print count
        hexes_to_udaciousness(base, spread, target)


# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230) 
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000) 
#>>> 1 

# need to match or exceed the target
#print hexes_to_udaciousness(50000, 2, 150001)
#>>> 2 

# only 12 hexamesters (2 years) to world domination!
#print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) 
#>>> 12 

# more friends means faster world domination!
#print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
#>>> 10 
