for groot in range(1, 101):
    if groot % 15 == 0:
        print "FizzBuzz"
    elif groot % 5 == 0:
        print "Buzz"
    elif groot % 3 == 0:
        print "Fizz"
    else:
        print groot


import random
my_randoms = random.sample(range(100), 15)
# This generates a random list to test (so the answers are basicallly impossible to fake.
print my_randoms

test_list=[1,2,3,100001]  # Use a test list to check your functions
odd_list = []  # Create the empty list OUTSIDE of the function, so that you can use it OUTSIDE of the function.
def find_odds(input):
    for thingy in input:
        if thingy % 2 == 1:
            print thingy

find_odds(test_list)

def odd_sum(input):
   for thingy in input:
       if thingy % 2 == 1:
           odd_list.append(thingy)
   print sum(odd_list)

odd_sum(test_list)