import time

a = input("Give me a number!")

if a>0:
    while a > 0:
        print str(a) + "..."
        a = a-1
        time.sleep(1)
else:
    while a<0:
        print str(a) + "..."
        a = a +1
        time.sleep(1)
print "Done with Python!"