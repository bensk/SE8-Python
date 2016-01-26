test_list = [1,2,3,1001]
odds_list = []
def find_odds(input):
    for x in input:
        if x %2==1:
            odds_list.append(x)
            print x
find_odds(test_list)
print "The sum of the odds is" + str(sum(odds_list))