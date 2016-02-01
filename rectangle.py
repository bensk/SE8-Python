def rectangle():
<<<<<<< Updated upstream
    import time
    x = int(input("How wide?"))
    y = int(input("How tall?"))
    for numbers in range(1,y):
        print "$" * x
    time.sleep(.01)

=======
    x = input("How wide?")
    y = input("How tall?")
    for numbers in range(y):
        print "*" * x
>>>>>>> Stashed changes
rectangle()