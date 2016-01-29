def rectangle():
    import time
    x = int(input("How wide?"))
    y = int(input("How tall?"))
    for numbers in range(1,y):
        print "$" * x
    time.sleep(.01)

rectangle()