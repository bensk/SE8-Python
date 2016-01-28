# Can we read this?
# Let's get started. I want to review how to print every number 1-100, so...
def fizz_buzz():
    for x in range(1,101):
        if x % 20 == 0:
            print "Welcome to the party, Rich"
        elif x % 2 ==0 and x % 7 == 0:
            print "Whoooo party"
        elif x "b% 2 == 0 :
            print "banana"
        elif x % 7 ==0:
            print "not so fast Amerie"
        # elif x % 2 == 0 and x % 7 ==0: this should go first!
        #     print "WHOOOO PARTY"

        else:
            print x
fizz_buzz()