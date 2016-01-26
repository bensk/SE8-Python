import random
my_randoms = random.sample(range(100), 15)

print my_randoms

def find_odds(       ):
    for numbers in x:
        if numbers % 2 == 1:
            print numbers

def odd_sum(x):
    odd_list = []
    for numbers in x:
        if numbers % 2 == 1:
            odd_list.append(numbers)
    return sum(odd_list)

def even_sum(x):
    even_list = []
    for numbers in x:
        if numbers % 2 == 0:
            even_list.append(numbers)
    return sum(even_list)

print "The odd numbers are:"
find_odds(my_randoms)
print "The sum of the even numbers is " + str(even_sum(my_randoms))
print "The sum of the odd numbers is " + str(odd_sum(my_randoms))


list_7_11 = []
def seven_eleven(input):
    for number in input:
        if number % 3 == 0 or number % 5 == 0:
            print number
seven_eleven([1,3,7,5,63,4,20,60])