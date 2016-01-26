def seven_eleven(que):
    for pancake in que:
        if pancake%7==0 or pancake%11==0:
            print pancake

seven_eleven([7,23,22,77,43,42])

# Meeting Standards
test_list=[1,2,3,100001]

# Exceeding Standards
import random
my_randoms = random.sample(range(100), 15)
print my_randoms
