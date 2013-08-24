## Question 4: Remove Tags
#
## When we add our words to the index, we don't really want to include
## html tags such as <body>, <head>, <table>, <a href="..."> and so on.
#
## Write a procedure, remove_tags, that takes as input a string and returns
## a list of words, in order, with the tags removed. Tags are defined to be
## strings surrounded by < >. Words are separated by whitespace or tags. 
## You may assume the input does not include any unclosed tags, that is,  
## there will be no '<' without a following '>'.
#
#def remove_tags(content):
#    result = []
#    while(len(content) > 0):
#        start = content.find('<')
#        if start == -1:
#            result.extend(content.strip().split(' '))
#            break
#        else:
#            end = content.find('>', start+1)
#            temp = content[:start].strip()
#            if len(temp) != 0:
#                result.extend(temp.split(' '))
#            content = content[(end+1):]
#    return result
#    
#print remove_tags('This <i>line</i> has <em>lots</em> of <b>tags</b>.')
##>>> ['This', 'line', 'has', 'lots', 'of', 'tags', '.']
#
#print remove_tags('''<h1>Title</h1><p>This is a
#                    <a href="http://www.udacity.com">link</a>.<p>''')
##>>> ['Title','This','is','a','link','.']
#
#print remove_tags('''<table cellpadding='3'>
#                     <tr><td>Hello</td><td>World!</td></tr>
#                     </table>''')
##>>> ['Hello','World!']
#
#print remove_tags("<hello><goodbye>")
##>>> []
#
#print remove_tags("This is plain text.")
##>>> ['This', 'is', 'plain', 'text.']

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

#def longest_repetition(nums):
#    if len(nums) == 0:
#        return None
#    counts = [nums[0], 1]
#    tempcounts = [nums[0], 1]
#    for num in nums[1:]:
#        if num == tempcounts[0]:
#            tempcounts[1] = tempcounts[1] + 1
#        else:
#            if tempcounts[1] > counts[1]:
#                counts[0] = tempcounts[0]
#                counts[1] = tempcounts[1]
#            tempcounts[0] = num
#            tempcounts[1] = 1
#    if tempcounts[1] > counts[1]:
#                counts[0] = tempcounts[0]
#                counts[1] = tempcounts[1]
#    return counts[0]
#            
#
#
#
##For example,
#print longest_repetition([2, 2, 3, 3, 3])
##3
#print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
## 3
#
#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
## b
#
#print longest_repetition([1,2,3,4,5])
## 1
#
#print longest_repetition([])
## None

# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

#def is_list(p):
#    return isinstance(p, list)
#
#def deep_reverse(p):
#    result = []
#    temp = p[:]
#    temp.reverse()
#    for item in temp:
#        if is_list(item):
#            result.append(deep_reverse(item))
#        else:
#            result.append(item)
#    return result
#
#
##For example,
#
#p = [1, [2, 3, [4, [5, 6]]]]
#print deep_reverse(p)
##>>> [[[[6, 5], 4], 3, 2], 1]
#print p
##>>> [1, [2, 3, [4, [5, 6]]]]
#
#q =  [1, [2,3], 4, [5,6]]
#print deep_reverse(q)
##>>> [ [6,5], 4, [3, 2], 1]
#print q
##>>> [1, [2,3], 4, [5,6]]

# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling 
# takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

#def stirling(n, k):
#    if n < k or k == 0:
#        return 0
#    elif n == k:
#        return 1
#    else:
#        return k * stirling(n - 1, k) + stirling(n - 1, k - 1)
#
#def bell(n):
#    sum = 0
#    for k in range(1, n + 1):
#        sum = sum + stirling(n, k)
#    return sum
#
#
#print stirling(1,1)
##>>> 1
#print stirling(2,1)
##>>> 1
#print stirling(2,2)
##>>> 1
#print stirling(2,3)
##>>>0
#
#print stirling(3,1)
##>>> 1
#print stirling(3,2)
##>>> 3
#print stirling(3,3)
##>>> 1
#
#print stirling(4,1)
##>>> 1
#print stirling(4,2)
##>>> 7
#print stirling(4,3)
##>>> 6
#print stirling(4,4)
##>>> 1
#
#print stirling(5,1)
##>>> 1
#print stirling(5,2)
##>>> 15
#print stirling(5,3)
##>>> 25
#print stirling(5,4)
##>>> 10
#print stirling(5,5)
##>>> 1
#
#print stirling(20,15)
##>>> 452329200
#
#print bell(1)
##>>> 1
#print bell(2)
##>>> 2
#print bell(3)
##>>> 5
#print bell(4)
##>>> 15
#print bell(5)
##>>> 52
#print bell(15)
##>>> 1382958545

# Two Gold Stars
# Question 2: Combatting Link Spam
 
# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.


def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

#print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

#print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

#print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}



