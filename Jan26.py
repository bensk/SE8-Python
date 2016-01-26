#0. test list
#1. Empty list
#2. A function
#3. loop
#4. conditional
# #5. put odd numbers into the empty list
#6. printed odd numbers
#7. called the function
#8. we found the sum of the odd list
test_list = [1,2,3,1001]
def odd_sum(input):
    odd_list = []
    for x in input:
        if x % 2 == 1:
            odd_list.append(x) # add x to odd_list
        print "SK is cool"
    print sum(odd_list)

odd_sum(test_list)