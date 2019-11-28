def probOfOne(value, tf):
    if tf == 1:
        print("Probability of False: " + str(1 - value))
    elif tf == 0:
        print("Probability of True: " + str(1 - value))

def probAnB():
    pass

def probAgivenB():
    pass

def main():
    probOfOne(0.30, 1)
    #exit()

if __name__ == "__main__":
    main()