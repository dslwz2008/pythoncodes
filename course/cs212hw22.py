#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    # Your code here
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in itertools.permutations(floors):
        if (Hopper is not top and 
            Kay is not bottom and
            Liskov is not bottom and Liskov is not top and
            abs(Liskov - Kay) > 1 and
            Perlis > Kay and
            abs(Ritchie - Liskov) > 1):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]
    #return result
    
if __name__ == '__main__':
    print floor_puzzle()
