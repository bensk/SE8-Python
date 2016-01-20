for groot in range(1, 101):
    if groot % 15 == 0:
        print "FizzBuzz"
    elif groot % 5 == 0:
        print "Buzz"
    elif groot % 3 == 0:
        print "Fizz"
    else:
        print groot
