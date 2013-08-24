#-*-coding:utf-8-*-
#Noah Gift
#Greedy Coin Match Algorithms

import optparse
import decimal
import sys

class Change():
    """Gives Correct Change Using As Many Greedy Match Algorithms as Possible"""

    def __init__(self, amount, verbose=False):
        self.amount = amount
        self.convert = int(self.amount*100)
        self.verbose = verbose
        self.coins = [1,5,10,25]
        self.coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
        if self.verbose:
            print "Converted Change Value: %s" % self.convert

    def printer(self,num,coin):
        """Printing Method For Recursive Results and While Results"""
        if num:
            if coin in self.coin_lookup:
                print num, self.coin_lookup[coin]

    def recursive_change(self, rem):
        """Greedy Coin Match with Recursion
        >>> c = Change(.71)
        >>> c.recursive_change(c.convert)
        2 quarters
        2 dimes
        1 pennies
        [1, 0, 2, 2]

        """
        if len(self.coins) == 0:
            return []
        coin = self.coins.pop()
        num, new_rem = divmod(rem, coin)
        self.printer(num,coin)
        return self.recursive_change(new_rem) + [num]

    def while_loop_change(self):
        """Greedy Coin Match with While Loop

        >>> c = Change(.71)
        >>> c.while_loop_change()
        2 quarters
        2 dimes
        1 pennies

        """
        coin = self.coins.pop()
        num, rem  = divmod(self.convert, coin)
        self.printer(num,coin)
        while rem > 0:
            coin = self.coins.pop()
            num, rem = divmod(rem, coin)
            self.printer(num,coin)

    def make_change_conditional(self):
        """Greedy Coin Match with Conditional Statements

        Return both number of coins and remainder

        >>> c = Change(.71)
        >>> c.make_change_conditional()
        (2, 21, 2, 1, 0, 0, 1)
        >>>

        """

        quarter, qrem = divmod(self.convert,25)

        #initialize values
        dime, drem = 0,0
        nickel, nrem = 0,0
        penny = 0

        #if remainder is dime or higher
        if qrem >= 10:
            dime, drem = divmod(qrem,10)
            if drem >= 5:
                nickel, nrem = divmod(drem,5)
                if nrem >= 1:
                    penny = nrem
            elif drem < 5:
                    penny = drem

        #if remainder is nickel or higher
        elif qrem >= 5:
            nickel, nrem = divmod(qrem,5)
            if nrem >= 1:
                penny = nrem

        #if remainder is penny or higher
        elif qrem > 0:
            penny = qrem

        return quarter, qrem, dime, drem, nickel, nrem, penny

    def full_results_printer(self):
        """Debug Print Method for Conditional Results"""
        quarter, qrem, dime, drem, nickel, nrem, \
        penny = self.make_change_conditional()
        print "Quarters %s: , Remainder: %s" % (quarter,qrem)
        print "Dimes %s: , Remainder: %s" % (dime,drem)
        print "Nickles %s: , Remainder: %s" % (nickel,nrem)
        print "Pennies %s:" % penny

    def conditional_printer(self):
        """Print Method For Conditional Results

        >>> c = Change(.71)
        >>> c.conditional_printer()
        Quarters 2
        Dimes 2
        Pennies 1

        """
        quarter, qrem, dime, drem, nickel, nrem, \
        penny = self.make_change_conditional()
        if quarter:
            print "Quarters %s" % quarter
        if dime:
            print "Dimes %s" % dime
        if nickel:
            print "Nickles %s " % nickel
        if penny:
            print "Pennies %s " % penny

def controller():
    p = optparse.OptionParser(description="Makes Change Using Greedy Coin Match",
                                prog = "pychange",
                                version = "pychange 0.1",
                                usage = "%prog [value] [options]")

    p.add_option("--full", "-f",
                action="store_true",
                help="Prints coin, plus remainder")

    p.add_option("--recursive", "-r",
                action="store_true",
                help="Prints coins with recursion")

    p.add_option("--loop", "-l",
                action="store_true",
                help="Prints coins with while loop")

    options, arguments = p.parse_args()
    if arguments:
        try:
            value = decimal.Decimal(arguments[0])
        except decimal.InvalidOperation:
            print "Please enter a valid number to make change"
            sys.exit(1)
        c = Change(value)
        if options.full:
            c.full_results_printer()
        elif options.recursive:
            c.recursive_change(c.convert)
        elif options.loop:
            c.while_loop_change()
        else:
            c.conditional_printer()
    else:
        p.print_help()

def main():
    controller()

if __name__ == "__main__":
    main()


