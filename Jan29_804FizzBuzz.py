# 1) FizzBuzz: Print every number from 1-100
# 2) For every multiple of 3, print Fizz, for every multiple of 5, print Buzz
# 3) For mulitples of 3 AND 5, print FizzBuzz

for x in range(1,101):
    if x % 3 == 0 and x % 5 ==0:
        print "FizzBuzz"
    elif x % 3 == 0:
        print "Fizz"
    elif x % 5 ==0: # elif is like another if
        print "Buzz"

    else:
        print x