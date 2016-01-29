def timer():
    import time

    max = input("What should I count down from?")
    for x in range(max):
        print max
        max = max - 1
        time.sleep(1)
    print "Boom!"

timer()

import datetime
print datetime.datetime.now().time()